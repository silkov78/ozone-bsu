from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staff.urls')),
]

urlpatterns += i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path('', include('main_app.urls')),
    path('', include('observations.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
