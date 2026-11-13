from django.db import models


class Observations(models.Model):
    '''Базовый класс наблюдений'''

    date = models.DateField(
        primary_key=True,
        unique=True,
        verbose_name='Дата'
    )

    @property
    def weekday(self):
        return self.date.strftime("%A")

    total_ozone_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Минск'
    )

    total_uvi_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Минск'
    )

    max_uvi_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Минск'
    )

    surface_ozone_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ПСО Минск'
    )

    total_ozone_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Гомель'
    )

    total_uvi_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Гомель'
    )

    max_uvi_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Гомель'
    )

    total_ozone_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Нарочь'
    )

    total_uvi_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Нарочь'
    )

    max_uvi_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Нарочь'
    )

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Наблюдения'
        ordering = ['-date']
