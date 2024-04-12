from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
import csv

from .models import AnnualReport, Observations
from .forms import ObservationsForm

from .services import ObservationsInMatrix


def observations_info_page(request):
    """Представление для страницы observations/info"""

    context = {
        "last_minsk_observations": Observations.objects.all().order_by('-date')[:7],
        "annual_reports": AnnualReport.objects.all()
    }

    return render(request, "observations-info.html", context)


def observations_download_page(request):
    """Представление для страницы observations/download"""

    if request.GET:
        form = ObservationsForm(request.GET)

        if form.is_valid():
            response = HttpResponse(content_type='text/csv')

            form_observations = ObservationsInMatrix(request.GET, Observations)
            observations_matrix = form_observations.get_observations_matrix()

            writer = csv.writer(response)
            for row in observations_matrix:
                writer.writerow(row)

            response['Content-Disposition'] = f'attachment; filename="observations.csv"'

            return response

    else:
        form = ObservationsForm()

    context = {'form': form}

    return render(request, "observations-download.html", context)
