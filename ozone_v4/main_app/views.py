from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from observations.views import observations_json
from staff.models import Worker
from .models import News, Article, Devices, Document, AnnualReport

# Подразделения — пока просто перечень (сущности в БД нет)
DEPARTMENTS = [
    "Лаборатория физики атмосферы",
    "Лаборатория биофотоники",
    "Лаборатория оптических средств измерений",
    "Информационно-аналитический центр",
    "Озонометрическая станция № 354 GAW",
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
        'devices': Devices.objects.all(),
        'articles': Article.objects.filter(status='PB').order_by('-published'),
        'annual_reports': AnnualReport.objects.all(),
    }
    return render(request, 'about.html', context)


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
