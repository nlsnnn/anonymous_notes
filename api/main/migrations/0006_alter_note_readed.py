# Generated by Django 4.2.1 on 2024-08-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_note_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='readed',
            field=models.BooleanField(default=0, verbose_name='Прочитано'),
        ),
    ]