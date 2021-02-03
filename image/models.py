from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import time


class ImageFolder(models.Model):
    title = models.CharField('Название', max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now=True)
    datetime_to_start_show = models.DateTimeField('Дата и время начала показа', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'imagefolder'
        verbose_name = 'Папка для изображений'
        verbose_name_plural = 'Папки для изображений'

def path_to_upload_image(instance, filename):
    return f"image/{time.time()}/{filename}"


class Image(models.Model):
    title = models.CharField('Название', max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey(ImageFolder, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to=path_to_upload_image)
    datetime_to_start_show = models.DateTimeField('Дата и время начала показа', blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'image'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
