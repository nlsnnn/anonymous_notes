# Generated by Django 4.2.1 on 2024-08-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_note_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time_create',
            field=models.DateField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
