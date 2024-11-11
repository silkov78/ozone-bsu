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
        'common_ozone_minsk',
        'uvi_minsk',
        'uvi_max_minsk',
        'surface_ozone_minsk'
    ]
