# Generated by Django 2.2.28 on 2023-04-27 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2023, 4, 28, 0, 23, 11, 850916), verbose_name='Опубликована')),
            ],
            options={
                'verbose_name': 'статья блога',
                'verbose_name_plural': 'статья блога',
                'db_table': 'Posts',
                'ordering': ['-posted'],
            },
        ),
    ]
