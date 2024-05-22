from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import News, Article, Devices, Document, DevicesCharacteristic, AnnualReport, ArticleFile

admin.site.site_header = 'ННИЦ МО БГУ'


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'tag', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['tag', 'status']
    save_as = True


class ArticleFileInline(admin.TabularInline):
    model = ArticleFile
    extra = 1


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ['title', 'time_creation', 'image_logo', 'status']
    readonly_fields = ['last_edit', 'time_creation', 'id']
    list_editable = ['status']
    save_as = True

    inlines = (ArticleFileInline, )


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = ['year', 'report_file']
    readonly_fields = ['last_edit']


@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ['name', 'description', 'document', 'time_creation']
    readonly_fields = ['last_edit', 'time_creation', 'id']


class DeviceTechCharacteristic(TranslationStackedInline):
    model = DevicesCharacteristic
    extra = 1
    classes = ('collapse', )


@admin.register(Devices)
class DevicesAdmin(TranslationAdmin):

    inlines = [
        DeviceTechCharacteristic
    ]

    readonly_fields = ('id', 'last_edit', 'time_creation')
