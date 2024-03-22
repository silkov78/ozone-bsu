from modeltranslation.translator import register, TranslationOptions
from .models import News, Article, Document, Devices, DevicesCharacteristic


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'body')


@register(Article)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'body')


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Devices)
class DevicesTranslationOptions(TranslationOptions):
    fields = ('name', 'subtitle', 'description')


@register(DevicesCharacteristic)
class DevicesTranslationOptions(TranslationOptions):
    fields = ('characteristic_name', 'characteristic_value')
