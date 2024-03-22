from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import News, Article, Devices, Document, DevicesCharacteristic

admin.site.site_header = 'ННИЦ МО'


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['status']
    save_as = True


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['status']
    save_as = True


@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ['name', 'description', 'document', 'time_creation']
    readonly_fields = ['last_edit', 'time_creation', 'id']


class DeviceTechCharacteristic(admin.TabularInline):
    model = DevicesCharacteristic
    extra = 1
    classes = ('collapse', )


@admin.register(Devices)
class DevicesAdmin(TranslationAdmin):

    inlines = [
        DeviceTechCharacteristic
    ]

    readonly_fields = ('id', 'last_edit', 'time_creation')
