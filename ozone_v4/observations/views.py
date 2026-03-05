from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
import csv

from .models import Observations
from .forms import ObservationsForm

from django.http import JsonResponse
from datetime import timedelta
from django.utils.timezone import now

from .services import ObservationsInMatrix


def observations_info_page(request):
    """Представление для страницы observations/info"""

    context = {
        "last_minsk_observations": Observations.objects.all().order_by('-date')[:7],
    }

    return render(request, "observations-info.html", context)


def observations_chart_data(request):

    range_type = request.GET.get("range", "week")

    qs = Observations.objects.all()

    if range_type == "week":
        qs = qs.filter(date__gte=now() - timedelta(days=7))

    elif range_type == "month":
        qs = qs.filter(date__gte=now() - timedelta(days=30))

    elif range_type == "year":
        qs = qs.filter(date__gte=now() - timedelta(days=365))

    elif range_type == "all":
        pass

    qs = qs.order_by("date")

    data = {
        "labels": [o.date.strftime("%Y-%m-%d") for o in qs],
        "total_ozone": [o.total_ozone_minsk for o in qs],
        "surface_ozone": [o.surface_ozone_minsk for o in qs],
        "uvi": [o.total_uvi_minsk for o in qs],
        "uvi_max": [o.max_uvi_minsk for o in qs],
    }

    return JsonResponse(data)


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
