from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.ImageFolder)
admin.site.register(models.Image)
