from django.urls import path

from .views import MainPageView
from .views import BlogPageView
from .views import NewsItemView
from .views import DocumetsPageView
from .views import AboutPageView


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page-url'),
    path('blog/', BlogPageView.as_view(), name='blog-page-url'),
    path('blog/<int:pk>/', NewsItemView.as_view(), name='news-item-url'),
    path('documents/', DocumetsPageView.as_view(), name='documents-page-url'),
    path('about/', AboutPageView.as_view(), name='about-page-url')
]