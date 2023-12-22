from django.db import models


class DailyMeasure(models.Model):
    """Класс для записи измерений метеопараметров в БД по датам"""

    date_field = models.DateField(verbose_name='Дата')
    weekday_field = models.CharField(max_length=9, verbose_name='День недели')

    common_ozone = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Общее содержание озона, единицы Добсона'
    )

    ultraviolet_index = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ индекс'
    )

    ultraviolet_max = models.FloatField(
        null=True,
        blank=True,
        verbose_name='УФ макс. '
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    @property
    def define_weekday(self):
        weekday_dict = {
            'Monday': 'Пн',
            'Tuesday': 'Вт',
            'Wednesday': 'Ср',
            'Thursday': 'Чт',
            'Friday': 'Пт',
            'Saturday': 'Сб',
            'Sunday': 'Вс',
        }
        return weekday_dict[self.date_field.strftime("%A")]

    def save(self, *args, **kwargs):
        self.weekday_field = self.define_weekday
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.weekday_field} | {self.date_field}'

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-date_field']


class AnnualReport(models.Model):
    year = models.IntegerField(verbose_name='Год')
    report_file = models.FileField(
        upload_to='observations/reports',
        verbose_name='Файл отчёта'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'Отчёт за {self.year} год'

    class Meta:
        verbose_name = 'Годовой отчёт'
        verbose_name_plural = 'Годовые отчёты'
        ordering = ['-year']
