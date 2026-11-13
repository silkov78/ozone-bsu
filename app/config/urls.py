from django.contrib import admin
from django.db import connection
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

def healthz(request):
    """Проверка живости для docker healthcheck: приложение + доступность БД."""
    try:
        connection.ensure_connection()
    except Exception:
        return HttpResponse('db error', status=503, content_type='text/plain')
    return HttpResponse('ok', content_type='text/plain')


urlpatterns = [
    path('healthz/', healthz),
    path('', include('staff.urls')),
]

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('', include('main_app.urls')),
    path('', include('staff.urls_html')),
    path('', include('observations.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
