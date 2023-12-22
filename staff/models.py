from django.db import models


class Worker(models.Model):
    '''Основная информация о сотруднике'''

    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество')

    photo = models.ImageField(
        upload_to='staff/workers_photos',
        verbose_name='Фото работника'
    )

    ordering = models.FloatField(
        default=42,
        verbose_name='Показан(а) на странице'
    )

    academic_rank = models.CharField(
        max_length=100,
        verbose_name='Учёное звание'
    )

    position = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name='Должность в институте'
    )

    mail = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Рабочая почта'
    )

    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Телефон'
    )

    adress = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name='Адресс'
    )

    google_academy = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Google academy'
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
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['ordering']


class Education(models.Model):
    '''Информация об образовании сотрудника'''

    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='education',
    )

    study_finishing = models.IntegerField(verbose_name='Год окончания')
    study_description = models.CharField(
        max_length=300,
        verbose_name='Информация об образовании'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.worker} {self.study_finishing}'

    class Meta:
        verbose_name = 'Сотрудник: образование'
        verbose_name_plural = 'Сотрудники: образование'
        ordering = ['worker', 'study_finishing']


class Career(models.Model):
    '''Информация о карьере сотрудника.
       Сортировка по полю: career_start.
    '''

    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='career',
    )

    career_start = models.IntegerField(verbose_name='Начало карьерного этапа')
    career_period = models.CharField(max_length=30, verbose_name='Период работы')

    career_description = models.CharField(
        max_length=300,
        verbose_name='Информация о работе'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.worker} {self.career_start}'

    class Meta:
        verbose_name = 'Сотрудник: карьера'
        verbose_name_plural = 'Сотрудники: карьера'
        ordering = ['worker', 'career_start']


class Reward(models.Model):
    '''Информация о наградах сотрудника.
       Сортировка по полю: .
    '''

    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='rewards',
    )

    reward_year = models.IntegerField(verbose_name='Год')

    reward_description = models.CharField(
        max_length=300,
        verbose_name='Информация о награде'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.worker} {self.reward_year}'

    class Meta:
        verbose_name = 'Сотрудник: награды'
        verbose_name_plural = 'Сотрудники: награды'
        ordering = ['worker', 'reward_year']


class ScienceInterest(models.Model):
    '''Информация о научных сотрудника.
       Сортировка по полю: id.
    '''

    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='science_interests',
    )

    science_interest = models.CharField(
        max_length=300,
        verbose_name='Научные интересы'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.worker} {self.science_interest}'

    class Meta:
        verbose_name = 'Сотрудник: научные интересы'
        verbose_name_plural = 'Сотрудники: научные интересы'
        ordering = ['worker', 'id']


class Publication(models.Model):
    '''Информация о научных публикациях сотрудника.
       Сортировка по полю publication_year.
    '''

    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name='publications',
    )

    publication_year = models.IntegerField(verbose_name='Год публикации')

    publication_description = models.TextField(
        max_length=600,
        verbose_name='Публикация'
    )

    publication_link = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Ссылка на публикацию'
    )

    last_edit = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )

    def __str__(self):
        return f'{self.worker} {self.publication_year}'

    class Meta:
        verbose_name = 'Сотрудник: публикации'
        verbose_name_plural = 'Сотрудники: публикации'
        ordering = ['worker', '-publication_year']
