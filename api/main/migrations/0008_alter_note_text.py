# Generated by Django 4.2.1 on 2024-08-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_note_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(max_length=180, verbose_name='Текст'),
        ),
    ]
