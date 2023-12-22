from django.urls import path

from .views import ObservPageView
from .views import DailyMeasuresAPIList
from .views import AnnualReportsAPIList


urlpatterns = [
    path('observations/', ObservPageView.as_view(), name='observ-url'),
    path('api/v1/daily_measures/', DailyMeasuresAPIList.as_view(), name='daily-measures-url'),
    path('api/v1/daily_measures/?format=json', DailyMeasuresAPIList.as_view(), name='daily-measures-json-url'),
    path('api/v1/annual_reports/', AnnualReportsAPIList.as_view())
]