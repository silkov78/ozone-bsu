from django.db import models
from django.utils.translation import gettext_lazy as _
from os.path import basename


class BasePost(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        null=False,
        blank=False
    )
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')

    image_logo = models.ImageField(
        upload_to='main/news',
        verbose_name='Фотография',
    )

    body = models.TextField(verbose_name='Содержание')

    published = models.DateField(
        verbose_name='Опубликовано для пользователя'
    )

    STATUS_CHOICES = (
        ('DF', 'Черновик'),
        ('PB', 'Опубликовано')
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='PB',
        verbose_name='Статус новости'
    )

    time_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено в БД'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    class Meta:
        abstract = True
        ordering = ['-published']


class News(BasePost):

    TAGS = (
        ("WE", _("О нас")),
        ("SCI", _("Наука")),
    )

    tag = models.CharField(
        max_length=3,
        choices=TAGS,
        default='WE',
        verbose_name='Тэг'
    )

    def __str__(self):
        return f'News | {self.title} | {self.published}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']


class Article(BasePost):

    body = models.TextField(
        verbose_name='Содержание',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Article | {self.title} | {self.published}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_creation']


class ArticleFile(models.Model):
    """Файлы, прикрепляемые к статьям (Article)"""

    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name="article_files"
    )

    file = models.FileField(
        upload_to="main/base_post_attach",
        verbose_name="Файл"
    )

    def filename(self):
        return basename(self.file.name)

    def __str__(self):
        return f'{self.article} | {self.pk}'

    class Meta:
        verbose_name = 'Файл к Статье'
        verbose_name_plural = 'Файлы к Статьям'
        ordering = ['article']


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


class Document(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    description = models.TextField(
        max_length=455,
        null=True,
        blank=True,
        verbose_name='Описание'
    )

    document = models.FileField(
        upload_to='main/documents',
        verbose_name='Файл документа'
    )

    time_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено в БД'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Документация'
        verbose_name_plural = 'Документация'
        ordering = ['-time_creation']


class Devices(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    subtitle = models.CharField(max_length=200, verbose_name='Предназначение')

    description = models.TextField(max_length=1500, verbose_name='Описание')

    main_image = models.ImageField(
        upload_to='main/devices',
        verbose_name='Главная фотография'
    )

    time_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлен в БД'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Прибор'
        verbose_name_plural = 'Приборы'
        ordering = ['-time_creation']


class DevicesCharacteristic(models.Model):
    ''' Технические характеристики прибора'''

    device = models.ForeignKey(
        Devices,
        on_delete=models.CASCADE,
        verbose_name='Прибор',
        related_name='characteristics'
    )

    characteristic_name = models.CharField(
        max_length=70,
        verbose_name='Характеристика'
    )

    characteristic_value = models.CharField(
        max_length=20,
        verbose_name='Значение'
    )

    time_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлен в БД'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.device}|{self.characteristic_name}'

    class Meta:
        verbose_name = 'Характеристика прибора'
        verbose_name_plural = 'Характеристики прибора'
        ordering = ['device', '-time_creation']
