from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import time
from user.models import MyLocalUser

class VideoFolder(models.Model):
    title = models.CharField('Название', max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now=True)
    datetime_to_start_show = models.DateTimeField('Дата и время начала показа', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'videofolder'
        verbose_name = 'Папка для видео'
        verbose_name_plural = 'Папки для видео'


def path_to_upload_video(instance, filename):
    return f"video/{time.time()}/{filename}"


class Video(models.Model):
    title = models.CharField('Название', max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey(VideoFolder, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField(upload_to=path_to_upload_video)
    datetime_to_start_show = models.DateTimeField('Дата и время начала показа', blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Все видео'
