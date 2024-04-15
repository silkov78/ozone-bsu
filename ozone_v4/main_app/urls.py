from django.urls import path

from .views import *


urlpatterns = [
    path('', main_page, name='main-page-url'),
    path('blog/', BlogPageView.as_view(), name='blog-page-url'),
    path('blog/<int:pk>/', NewsItemView.as_view()),
    path('articles/', articles_page_view, name='articles-page-url'),
    path('articles/<int:pk>/', ArticlesItemView.as_view(), name='articles-item-url'),
    path('search/', search_page, name='search-page-url'),
    path('search/<int:pk>/', NewsItemView.as_view(), name='search-item-url'),
    path('devices/', DevicesPageView.as_view(), name='devices-page-url'),
    path('devices/<int:pk>/', DeviceItemView.as_view(), name='devices-item-url'),
    path('documents/', DocumetsPageView.as_view(), name='documents-page-url'),
    path('about/', AboutPageView.as_view(), name='about-page-url'),
    path('cookies/', cookies_page, name='cookies-page-url')
]
