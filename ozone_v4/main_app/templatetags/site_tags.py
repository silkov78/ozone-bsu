"""Фильтры для шаблонов нового фронта."""
import re
from urllib.parse import urlparse

from django import template
from django.template.defaultfilters import linebreaks_filter, urlize
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

register = template.Library()

_TAG = re.compile(r"<(p|br|ul|ol|h[1-6]|blockquote|figure|table|a|strong|em)\b", re.I)


@register.filter
def rich_text(value):
    """Текст новости/статьи: HTML из CKEditor — как есть, старый простой текст — абзацы + ссылки."""
    if not value:
        return ""
    if _TAG.search(value):
        return mark_safe(value)
    return linebreaks_filter(urlize(value, autoescape=True), autoescape=False)


@register.filter
def excerpt(value, length=160):
    """Начало текста без HTML — вместо подзаголовка в карточках."""
    text = re.sub(r"\s+", " ", strip_tags(value or "")).strip()
    length = int(length)
    if len(text) <= length:
        return text
    return text[:length].rsplit(" ", 1)[0] + "…"


@register.filter
def domain(url):
    """https://www.nasa.gov/... -> nasa.gov"""
    try:
        host = urlparse(url).hostname or ""
    except ValueError:
        return ""
    return host[4:] if host.startswith("www.") else host


@register.filter
def file_ext(field):
    """Расширение файла для значка: PDF, DOCX…"""
    name = getattr(field, "name", "") or ""
    return name.rsplit(".", 1)[-1].upper() if "." in name else "FILE"


@register.filter
def safe_size(field):
    """Размер файла; пустая строка, если файла нет на диске."""
    from django.template.defaultfilters import filesizeformat
    try:
        return filesizeformat(field.size)
    except (OSError, ValueError):
        return ""
