# Generated by Django 4.2.1 on 2024-08-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=10, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('author', models.CharField(max_length=20, verbose_name='Автор')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('readed', models.BooleanField(verbose_name='Прочитано')),
            ],
        ),
    ]
