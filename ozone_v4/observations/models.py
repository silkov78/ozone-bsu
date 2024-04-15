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

    common_ozone_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Гомель'
    )

    common_ozone_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ОСО Нарочь'
    )

    uf_index_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Минск'
    )

    uf_index_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Гомель'
    )

    uf_index_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-индекс Нарочь'
    )

    uf_max_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Минск'
    )

    uf_max_homel = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Гомель'
    )

    uf_max_naroch = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ-макс Нарочь'
    )

    ground_ozone_minsk = models.FloatField(
        null=True,
        blank=True,
        verbose_name='ПСО Минск'
    )

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Наблюдения'
        ordering = ['-date']
