from django.contrib import admin

from .models import DailyMeasure, AnnualReport


# Register your models here.
@admin.register(DailyMeasure)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['date_field', 'weekday_field']
    readonly_fields = ['weekday_field', 'last_edit']


@admin.register(AnnualReport)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ['year','report_file']
    readonly_fields = ['last_edit']
