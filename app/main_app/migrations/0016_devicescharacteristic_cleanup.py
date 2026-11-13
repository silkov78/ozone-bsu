"""Чистка названий характеристик: убрать двоеточия в конце, восстановить
обрезанное (лимит 70 символов) название у ПИОН-АКВА."""
from django.db import migrations


def cleanup(apps, schema_editor):
    C = apps.get_model('main_app', 'DevicesCharacteristic')
    for c in C.objects.all():
        name = (c.characteristic_name or '').rstrip(': ')
        value = (c.characteristic_value or '').rstrip('. ') if c.characteristic_value.endswith('часа.') else c.characteristic_value
        if name.startswith('Время автономной работы от штатного li-ion'):
            name = 'Время автономной работы (Li-ion аккумулятор 5600 мАч)'
        if (name, value) != (c.characteristic_name, c.characteristic_value):
            c.characteristic_name = c.characteristic_name_ru = name
            c.characteristic_value = c.characteristic_value_ru = value
            c.save()


class Migration(migrations.Migration):
    dependencies = [('main_app', '0015_devicescharacteristic_value_length')]
    operations = [migrations.RunPython(cleanup, migrations.RunPython.noop)]
