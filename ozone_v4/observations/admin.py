from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from .models import Observations


class ObservationsResource(ModelResource):

    class Meta:
        model = Observations
        import_id_fields = ("date",)


@admin.register(Observations)
class ObservationsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ObservationsResource]
    list_display = [
        'date',
        'total_ozone_minsk',
        'total_uvi_minsk',
        'max_uvi_minsk',
        'surface_ozone_minsk'
    ]
