# Generated by Django 4.2.1 on 2024-08-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_note_readed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
    ]
