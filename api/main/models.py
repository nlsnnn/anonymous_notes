from django.db import models


class Note(models.Model):
    num = models.CharField(verbose_name='ID', max_length=36, blank=True, null=True, unique=True)
    text = models.TextField(verbose_name='Текст')
    author = models.CharField(verbose_name='Автор', max_length=20)
    readed = models.BooleanField(verbose_name='Прочитано', default=0)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')