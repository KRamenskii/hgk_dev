from django.contrib import admin
from .models import PageVisit, ButtonClick

@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'ip_address', 'timestamp')
    list_filter = ('page_url', 'timestamp')

@admin.register(ButtonClick)
class ButtonClickAdmin(admin.ModelAdmin):
    list_display = ('button_id', 'page_url', 'ip_address', 'timestamp')
    list_filter = ('page_url', 'button_id', 'timestamp')