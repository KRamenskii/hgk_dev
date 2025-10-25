from django.shortcuts import render
from .models import (
    SiteSettings, Service, Advantage
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

    context = {
        'settings': settings,
        'services': services,
        'advantages': advantages,
    }
    return render(request, 'website/index.html', context)