from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from .models import Observations, AnnualReport


class ObservationsResource(ModelResource):

    class Meta:
        model = Observations
        import_id_fields = ("date",)


@admin.register(Observations)
class ObservationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ObservationsResource]
    list_display = [
        'date',
        'weekday',
        'common_ozone_minsk',
        'common_ozone_homel',
        'common_ozone_naroch'
    ]


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ['year', 'report_file']
    readonly_fields = ['last_edit']
