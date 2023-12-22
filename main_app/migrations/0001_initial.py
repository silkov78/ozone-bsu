# Generated by Django 4.2.8 on 2023-12-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='main/devices', verbose_name='Фотография')),
                ('time_creation', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен изменение')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
            ],
            options={
                'verbose_name': 'Прибор',
                'verbose_name_plural': 'Приборы',
                'ordering': ['-time_creation'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Подзаголовок')),
                ('image_logo', models.ImageField(upload_to='main/news', verbose_name='Фотография')),
                ('body', models.TextField(verbose_name='Содержание новости')),
                ('published', models.DateField(verbose_name='Опубликовано для пользователя')),
                ('status', models.CharField(choices=[('DF', 'Черновик'), ('PB', 'Опубликовано')], default='PB', max_length=2, verbose_name='Статус новости')),
                ('time_creation', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено в БД')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_creation'],
            },
        ),
    ]
