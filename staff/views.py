from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.views.generic import ListView
from django.views.generic import DetailView

from .serializeres import WorkersListSerializer
from .serializeres import WorkersPageSerializer

from .models import Worker

class WorkersListView(ListView):
    '''Контроллер для html-страницы списка сотрудников'''

    template_name = 'team.html'
    queryset = Worker.objects.all()


class WorkersAPIList(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkersListSerializer


class WorkersDetailView(DetailView):
    '''Контроллер для html-страницы списка сотрудников'''

    template_name = 'team-single.html'
    model = Worker


class WorkersAPIDetail(RetrieveAPIView):
    '''API-контроллер для страницы отдельного сотрудника'''

    queryset = Worker.objects.all()
    serializer_class = WorkersPageSerializer
    lookup_field = 'id'


