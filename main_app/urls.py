from django.urls import path

from .views import MainPageView
from .views import BlogPageView
from .views import NewsItemView
from .views import DocumetsPageView
from .views import AboutPageView
from .views import DevicesPageView
from .views import DeviceItemView




urlpatterns = [
    path('', MainPageView.as_view(), name='main-page-url'),
    path('blog/', BlogPageView.as_view(), name='blog-page-url'),
    path('blog/<int:pk>/', NewsItemView.as_view(), name='news-item-url'),
    path('devices/', DevicesPageView.as_view(), name='devices-page-url'),
    path('devices/<int:pk>/', DeviceItemView.as_view(), name='devices-item-url'),
    path('documents/', DocumetsPageView.as_view(), name='documents-page-url'),
    path('about/', AboutPageView.as_view(), name='about-page-url')
]