from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
]