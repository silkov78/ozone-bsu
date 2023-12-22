from django.contrib import admin

from .models import News
from .models import Devices
from .models import Document


admin.site.site_header = 'ННИЦ МО'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['status']
    save_as = True


@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'time_creation', 'image']
    readonly_fields = ['last_edit', 'time_creation']


@admin.register(Document)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','document', 'time_creation']
    readonly_fields = ['last_edit', 'time_creation', 'id']

