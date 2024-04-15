from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .models import News, Article, Devices, Document, AnnualReport


def main_page(request):
    context = {
        'about_us_news': News.objects.filter(status='PB', tag="WE").order_by('-published')[0:3],
        'science_news': News.objects.filter(status='PB', tag="SCI").order_by('-published')[0:3],
        'devices': Devices.objects.all()[0:6]
    }

    return render(request, 'index.html', context)


# ----------------------------------------------------

class BlogPageView(ListView):
    template_name = 'blog.html'
    paginate_by = 4

    def get_queryset(self):
        return News.objects.filter(status='PB').order_by('-published')


class NewsItemView(DetailView):
    model = News
    template_name = 'blog-single.html'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('blog-page-url'))


# class ArticlesPageView(ListView):
#     template_name = 'articles.html'
#     paginate_by = 4
#
#     def get_queryset(self):
#         return Article.objects.filter(status='PB').order_by('-published')


def articles_page_view(request):
    articles_list = Article.objects.filter(status='PB').order_by('-published')
    paginator = Paginator(articles_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "annual_reports": AnnualReport.objects.all()
    }
    return render(request, "articles.html", context)


class ArticlesItemView(DetailView):
    model = Article
    template_name = 'article-single.html'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('articles-page-url'))


def search_page(request):
    search_query = request.GET.get("search")
    object_list = News.objects.filter(
        Q(title__icontains=search_query) | \
        Q(subtitle__icontains=search_query) | \
        Q(body__icontains=search_query), \
        status='PB'
    )

    context = {'object_list': object_list}

    return render(request, 'search.html', context)


# ------------------------------------------------------------
class DevicesPageView(ListView):
    template_name = 'devices.html'
    model = Devices


class DeviceItemView(DetailView):
    model = Devices
    template_name = 'devices-single.html'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('devices-page-url'))


# ----------------------------------------------------

class DocumetsPageView(ListView):
    template_name = 'documents.html'
    model = Document


# ----------------------------------------------------
class AboutPageView(TemplateView):
    template_name = 'about.html'
    # model = Document


# ----------------------------------------------------
def cookies_page(request):
    return render(request, 'cookies.html')
