from django.urls import path

from .views import *


urlpatterns = [
    path('observations/info/', observations_info_page, name='observ-info-url'),
    path('observations/download/', observations_download_page, name='observ-download-url'),
]
