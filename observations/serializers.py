from rest_framework.serializers import ModelSerializer

from .models import DailyMeasure
from .models import AnnualReport


class DailyMeasureSerializer(ModelSerializer):
    class Meta:
        model = DailyMeasure
        fields = [
            'date_field',
            'common_ozone',
            'ultraviolet_index',
            'ultraviolet_max',
        ]


class AnnualReportSerializer(ModelSerializer):
    class Meta:
        model = AnnualReport
        fields = [
            'year',
            'report_file',
        ]
