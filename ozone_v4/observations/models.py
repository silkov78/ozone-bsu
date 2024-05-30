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

    common_ozone_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Минск'
    )

    surface_ozone_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ПСО Минск'
    )

    uvi_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Минск'
    )

    uvi_max_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Минск'
    )

    common_ozone_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Гомель'
    )

    uvi_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Гомель'
    )

    uvi_max_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Гомель'
    )

    common_ozone_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Нарочь'
    )

    uvi_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Нарочь'
    )

    uvi_max_naroch = models.FloatField(
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
