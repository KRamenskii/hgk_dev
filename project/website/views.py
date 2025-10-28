from django.shortcuts import render
from django.conf import settings as django_settings
from .models import (
    SiteSettings, Service, Advantage, CoverageStat, DeliveryPoint
)

def index(request):
    """Главная страница"""
    # Получаем настройки сайта
    try:
        settings = SiteSettings.objects.first()
    except:
        settings = None
    
    services = Service.objects.filter(is_active=True).order_by('order')
    advantages = Advantage.objects.filter(is_active=True).order_by('order')
    coverage_stats = CoverageStat.objects.filter(is_active=True).order_by('order')
    delivery_points = DeliveryPoint.objects.filter(active=True)

    hero_stats = {
        'years': '15+',
        'clients': '1000+',
        'support': '24/7',
        'quality': '100%'
    }

    context = {
        'settings': settings,
        'services': services,
        'advantages': advantages,
        'coverage_stats': coverage_stats,
        'hero_stats': hero_stats,
        'delivery_points': list(delivery_points.values("name", "description", "latitude", "longitude")),
        'YANDEX_MAP_API_KEY': django_settings.YANDEX_MAP_API_KEY,
    }
    return render(request, 'website/index.html', context)