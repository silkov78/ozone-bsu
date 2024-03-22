from django.urls import path

from .views import *


urlpatterns = [
    path('observations/', observations_page, name='observ-url'),
]
