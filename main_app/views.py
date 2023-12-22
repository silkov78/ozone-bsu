from django.views.generic import TemplateView, ListView, DetailView

from .models import News
from .models import Devices
from .models import Document


class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainPageView, self).get_context_data(*args, **kwargs)

        context['news'] = News.objects.filter(status='PB').order_by('-time_creation')[0:2]
        context['devices'] = Devices.objects.all()[0:6]

        return context


class BlogPageView(ListView):
    template_name = 'blog.html'
    paginate_by = 4

    def get_queryset(self):
        return News.objects.filter(status='PB').order_by('-time_creation')


class NewsItemView(DetailView):
    model = News
    template_name = 'blog-single.html'


class DocumetsPageView(ListView):
    template_name = 'documents.html'
    model = Document
