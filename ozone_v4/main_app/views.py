from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from observations.views import observations_json
from itertools import groupby

from staff.models import Worker, Publication
from .models import News, Article, Devices, Document, AnnualReport

# Подразделения — пока просто перечень (сущности в БД нет)
DEPARTMENTS = [
    _("Лаборатория физики атмосферы"),
    _("Лаборатория биофотоники"),
    _("Лаборатория оптических средств измерений"),
    _("Информационно-аналитический центр"),
    _("Озонометрическая станция № 354 GAW"),
]


def published_news():
    return News.objects.filter(status='PB').order_by('-published')


def main_page(request):
    context = {
        'news': published_news()[:3],
        # 90 дней + запас на задержку Гомеля/Нарочи
        'observations': observations_json(days=120),
    }
    return render(request, 'index.html', context)


def news_list(request):
    page = Paginator(published_news(), 9).get_page(request.GET.get('page'))
    return render(request, 'news.html', {'page_obj': page})


def news_item(request, pk):
    item = get_object_or_404(News, pk=pk, status='PB')
    more = published_news().exclude(pk=pk)[:3]
    return render(request, 'news-item.html', {'object': item, 'more': more})


def about_page(request):
    context = {
        'departments': DEPARTMENTS,
        'workers': Worker.objects.all(),
    }
    return render(request, 'about.html', context)


def science_page(request):
    pubs = Publication.objects.select_related('worker').order_by('-publication_year', 'worker__ordering')
    context = {
        'articles': Article.objects.filter(status='PB').order_by('-published'),
        'devices': Devices.objects.all(),
        'annual_reports': AnnualReport.objects.all(),
        # публикации сотрудников по годам: [(2026, [..]), (2025, [..]), ...]
        'publications_by_year': [(y, list(g)) for y, g in groupby(pubs, key=lambda p: p.publication_year)],
        'publications_count': pubs.count(),
    }
    return render(request, 'science.html', context)


def device_item(request, pk):
    device = get_object_or_404(Devices.objects.prefetch_related('characteristics'), pk=pk)
    return render(request, 'device.html', {'object': device})


def article_item(request, pk):
    article = get_object_or_404(Article.objects.prefetch_related('article_files'), pk=pk, status='PB')
    return render(request, 'article.html', {'object': article})


def documents_page(request):
    return render(request, 'documents.html', {'documents': Document.objects.all()})


def search_page(request):
    query = (request.GET.get('q') or request.GET.get('search') or '').strip()
    results = published_news().filter(Q(title__icontains=query) | Q(body__icontains=query)) if query else []
    return render(request, 'search.html', {'query': query, 'results': results})


def cookies_page(request):
    return render(request, 'cookies.html')
