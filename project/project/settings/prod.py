from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['xn--19-glc2a5c.xn--p1ai', 'www.xn--19-glc2a5c.xn--p1ai'])

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://xn--19-glc2a5c.xn--p1ai',
    'http://www.xn--19-glc2a5c.xn--p1ai',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'hgk_db'),
        'USER': os.environ.get('POSTGRES_USER', 'hgk_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'hgk_pass'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

LOGGING['root']['level'] = 'WARNING'