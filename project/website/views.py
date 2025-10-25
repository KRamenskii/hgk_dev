from django.shortcuts import render
from .models import (
    SiteSettings, Service
)

def index(request):
    """Главная страница"""
    # Получаем настройки сайта
    try:
        settings = SiteSettings.objects.first()
    except:
        settings = None
    
    services = Service.objects.filter(is_active=True).order_by('order')

    context = {
        'settings': settings,
        'services': services,
    }
    return render(request, 'website/index.html', context)