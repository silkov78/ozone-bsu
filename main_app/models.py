from django.db import models


class News(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')

    image_logo = models.ImageField(
        upload_to='main/news',
        verbose_name='Фотография'
    )

    body = models.TextField(verbose_name='Содержание новости')

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

    def __str__(self):
        return f'{self.title} | {self.time_creation.strftime("%Y-%m-%d %H:%M:%S")}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_creation']


class Document(models.Model):

    name = models.CharField(max_length=150,  verbose_name='Название')

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


class TechCharacteristic(models.Model):
    ''' Технические характеристики прибора'''

    device = models.ForeignKey(
        Devices,
        on_delete=models.CASCADE,
        verbose_name='Прибор'
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
        return f'{self.name}'

    class Meta:
        verbose_name = 'Характеристика прибора'
        verbose_name_plural = 'Характеристики прибора'
        ordering = ['device', '-time_creation']


class GalleryImage(models.Model):
    '''Галлерея фотографий прибора'''

    device = models.ForeignKey(
        Devices,
        on_delete=models.CASCADE,
        verbose_name='Прибор'
    )

    gallery_image = models.ImageField(
        upload_to='main/devices_gallery/',
        verbose_name='Фотография'
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
        return f'{self.characteristic_name}'

    class Meta:
        verbose_name = 'Галерея прибора'
        verbose_name_plural = 'Галереи приборов'
        ordering = ['device', '-time_creation']