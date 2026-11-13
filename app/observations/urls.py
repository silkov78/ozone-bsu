from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('observations/', views.observations_page, name='observations-url'),
    path('observations/export/', views.observations_export, name='observations-export-url'),
    path('observations/chart-data/', views.observations_chart_data, name='observ-chart-data'),

    # старые адреса -> новые (301)
    path('observations/info/', RedirectView.as_view(pattern_name='observations-url', permanent=True)),
    path('observations/download/', RedirectView.as_view(pattern_name='observations-url', permanent=True)),
]
