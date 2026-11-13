from django.urls import path

from .views import WorkersAPIList, WorkersAPIDetail

# JSON-API (вне языковых префиксов)
urlpatterns = [
    path('api/staff/v1/workers/', WorkersAPIList.as_view()),
    path('api/staff/v1/workers/<int:id>/', WorkersAPIDetail.as_view()),
]
