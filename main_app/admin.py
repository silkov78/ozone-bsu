from django.contrib import admin

from .models import News
from .models import Devices
from .models import Document
from .models import TechCharacteristic
from .models import GalleryImage



admin.site.site_header = 'ННИЦ МО'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['status']
    save_as = True


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description','document', 'time_creation']
    readonly_fields = ['last_edit', 'time_creation', 'id']



class DeviceTechCharacteristic(admin.TabularInline):
    model = TechCharacteristic
    extra = 1
    classes = ('collapse', )


# class DeviceGalleryImage(admin.TabularInline):
#     model = GalleryImage
#     extra = 1
#     classes = ('collapse', )


@admin.register(Devices)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        DeviceTechCharacteristic
        # DeviceGalleryImage
    ]

    # list_display = ['last_name', 'first_name',  'academic_rank', 'ordering', ]
    readonly_fields = ('id', 'last_edit', 'time_creation')
