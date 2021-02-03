from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.VideoFolder)
admin.site.register(models.Video)
