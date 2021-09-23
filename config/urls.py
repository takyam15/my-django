from pathlib import Path

import environ
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))

urlpatterns = [
    path('', include('account.urls')),
    path(env.get_value('ADMIN_URL', default='admin/'), admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
