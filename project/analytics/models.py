from django.db import models


class PageVisit(models.Model):
    page_url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    def __str__(self):
        return f"{self.page_url} — {self.timestamp:%Y-%m-%d %H:%M:%S}"


class ButtonClick(models.Model):
    button_id = models.CharField(max_length=100)
    page_url = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.button_id} — {self.timestamp:%Y-%m-%d %H:%M:%S}"