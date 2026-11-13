from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListAPIView, RetrieveAPIView


from .serializeres import WorkersListSerializer, WorkersPageSerializer
from .models import Worker


class WorkersAPIList(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkersListSerializer


def worker_page(request, pk):
    """Страница сотрудника."""
    worker = get_object_or_404(
        Worker.objects.prefetch_related('education', 'career', 'rewards', 'science_interests', 'publications'),
        pk=pk)
    return render(request, 'team-member.html', {'w': worker})


class WorkersAPIDetail(RetrieveAPIView):
    '''API-контроллер для страницы отдельного сотрудника'''

    queryset = Worker.objects.all()
    serializer_class = WorkersPageSerializer
    lookup_field = 'id'


