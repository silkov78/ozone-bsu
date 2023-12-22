from django.urls import path
# from django.conf.urls import url

# from rest_framework import routers

from .views import WorkersListView
from .views import WorkersAPIList
from .views import WorkersDetailView
from .views import WorkersAPIDetail


# router = routers.SimpleRouter()
# router.register()

urlpatterns = [
    path('staff/', WorkersListView.as_view(), name='workers-list-url'),
    path('staff/<pk>/', WorkersDetailView.as_view(), name='workers-detail-url'),

    path('api/staff/v1/workers/', WorkersAPIList.as_view()),
    path('api/staff/v1/workers/<int:id>/', WorkersAPIDetail.as_view())

]