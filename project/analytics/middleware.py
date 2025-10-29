from .models import PageVisit
from django.utils.deprecation import MiddlewareMixin


class AnalyticsMiddleware(MiddlewareMixin):
    EXCLUDED_PREFIXES = ('/admin', '/analytics', '/login', '/logout', '/static', '/media')

    WEBSITE_PREFIX = '/'   # поставь '/site/' если нужно

    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path

        # исключаем служебные пути
        if path.startswith(self.EXCLUDED_PREFIXES):
            return None

        # логируем только вебсайт (лендинг)
        if not path.startswith(self.WEBSITE_PREFIX):
            return None

        PageVisit.objects.create(
            page_url=path,
            ip_address=self._get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:1024],
        )
        return None

    def _get_client_ip(self, request):
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            return xff.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')