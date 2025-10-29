from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('stats/', views.stats_view, name='analytics_stats'),
    path('track_click/', views.track_click, name='track_click'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]