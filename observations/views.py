from django.views.generic.base import TemplateView
from rest_framework.generics import ListAPIView

from .serializers import DailyMeasureSerializer
from .serializers import AnnualReportSerializer
from .models import DailyMeasure
from .models import AnnualReport


class ObservPageView(TemplateView):
    template_name = 'observations.html'


class DailyMeasuresAPIList(ListAPIView):
    queryset = DailyMeasure.objects.all()
    serializer_class = DailyMeasureSerializer


class AnnualReportsAPIList(ListAPIView):
    queryset = AnnualReport.objects.all().order_by('year')
    serializer_class = AnnualReportSerializer
