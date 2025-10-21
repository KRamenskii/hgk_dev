from django.contrib import admin
from .models import (
    SiteSettings, Service, Advantage, CoverageStat, DeliveryPoint
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'additional_telephone', 'email']
    fieldsets = (
        ('Основная информация', {
            'fields': ('company_name', 'phone', 'additional_telephone', 'email', 'address', 'working_hours')
        }),
        ('Главная секция', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
    )
    
    def has_add_permission(self, request):
        # Только один экземпляр настроек
        return not SiteSettings.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'badge_text', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active', 'badge_text']
    ordering = ['order', 'title']


@admin.register(CoverageStat)
class CoverageStatAdmin(admin.ModelAdmin):
    list_display = ['title', 'number', 'icon', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']


@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude", "active")
    list_filter = ("active",)
    search_fields = ("name", "description")


# Кастомизация админ-панели
admin.site.site_header = "ХГК - Админ панель"
admin.site.site_title = "ХГК Админ"
admin.site.index_title = "Управление сайтом ХГК"