from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.db.models import Count
from django.utils.timezone import now, timedelta
from django.http import JsonResponse
from datetime import timedelta, date
from django.db.models.functions import TruncDate
import json
from .models import PageVisit, ButtonClick


@login_required
def stats_view(request):
    # Базовые queryset’ы
    visits_qs = PageVisit.objects.all()
    clicks_qs = ButtonClick.objects.all()

    # Фильтр по дате (опционально): /analytics/stats/?date=YYYY-MM-DD
    filter_date = request.GET.get("date")
    if filter_date:
        d = parse_date(filter_date)
        if d:
            visits_qs = visits_qs.filter(timestamp__date=d)
            clicks_qs = clicks_qs.filter(timestamp__date=d)

    # Таблицы (последние 50)
    page_visits = visits_qs.order_by('-timestamp')[:50]
    button_clicks = clicks_qs.order_by('-timestamp')[:50]

    # График за последние 7 дней (всегда 7 точек, с нулями для пустых дней)
    today = date.today()
    start_day = today - timedelta(days=6)
    days = [start_day + timedelta(days=i) for i in range(7)]

    visits_by_day = (
        PageVisit.objects
        .filter(timestamp__date__gte=start_day)
        .annotate(d=TruncDate('timestamp'))
        .values('d')
        .annotate(total=Count('id'))
    )
    clicks_by_day = (
        ButtonClick.objects
        .filter(timestamp__date__gte=start_day)
        .annotate(d=TruncDate('timestamp'))
        .values('d')
        .annotate(total=Count('id'))
    )

    v_map = {row['d']: row['total'] for row in visits_by_day}
    c_map = {row['d']: row['total'] for row in clicks_by_day}

    chart_labels = [d.strftime('%d.%m') for d in days]
    chart_visits = [v_map.get(d, 0) for d in days]
    chart_clicks = [c_map.get(d, 0) for d in days]

    context = {
        'page_visits': page_visits,
        'button_clicks': button_clicks,
        'visits_count': visits_qs.count(),
        'clicks_count': clicks_qs.count(),
        'filter_date': filter_date or "",
        'chart_labels': chart_labels,
        'chart_visits': chart_visits,
        'chart_clicks': chart_clicks,
    }
    return render(request, 'analytics/stats.html', context)


@csrf_exempt
def track_click(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            button_id = data.get("button_id")
            page_url = data.get("page_url")
            ip_address = request.META.get("REMOTE_ADDR")

            # Игнорируем клики на самой странице статистики
            if page_url.startswith("/analytics/stats"):
                return JsonResponse({"status": "ignored"})

            if button_id and page_url:
                ButtonClick.objects.create(
                    button_id=button_id,
                    page_url=page_url,
                    ip_address=ip_address
                )
                return JsonResponse({"status": "ok"})
            else:
                return JsonResponse({"status": "error", "message": "Missing data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid method"}, status=405)