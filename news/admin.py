from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.News)
admin.site.register(models.SectionNews)
admin.site.register(models.NewsCounter)
