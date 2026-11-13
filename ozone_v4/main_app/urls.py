from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.main_page, name='main-page-url'),
    path('news/', views.news_list, name='news-list-url'),
    path('news/<int:pk>/', views.news_item, name='news-item-url'),
    path('about/', views.about_page, name='about-page-url'),
    path('devices/<int:pk>/', views.device_item, name='devices-item-url'),
    path('articles/<int:pk>/', views.article_item, name='articles-item-url'),
    path('documents/', views.documents_page, name='documents-page-url'),
    path('search/', views.search_page, name='search-page-url'),
    path('cookies/', views.cookies_page, name='cookies-page-url'),

    # старые адреса -> новые (301)
    path('blog/', RedirectView.as_view(pattern_name='news-list-url', permanent=True, query_string=True)),
    path('blog/<int:pk>/', RedirectView.as_view(pattern_name='news-item-url', permanent=True)),
    path('search/<int:pk>/', RedirectView.as_view(pattern_name='news-item-url', permanent=True)),
    path('articles/', RedirectView.as_view(url='/about/#science', permanent=True)),
    path('devices/', RedirectView.as_view(url='/about/#devices', permanent=True)),
]
