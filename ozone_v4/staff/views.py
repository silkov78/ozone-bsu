from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView


from .serializeres import WorkersListSerializer, WorkersPageSerializer
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

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('workers-list-url'))


class WorkersAPIDetail(RetrieveAPIView):
    '''API-контроллер для страницы отдельного сотрудника'''

    queryset = Worker.objects.all()
    serializer_class = WorkersPageSerializer
    lookup_field = 'id'


