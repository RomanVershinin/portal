from django.db import models

# Create your models here.

from django.contrib.auth.models import User
#from user.models import MyLocalUser
import time

class SectionNews(models.Model):
    title = models.CharField('Раздел сайта', max_length=150)
    datetime_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'sectionnews'
        verbose_name = 'Раздел  новостей'
        verbose_name_plural = 'Разделы новостей'


def get_path_to_tiny_image(instance, filename):
    return "image/news/tiny_image/{}/{}".format(time.time(), filename)

class News(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Краткое описание', max_length=300)
    body = models.TextField('Статья (Новость)', max_length=10000)
    datetime_create = models.DateTimeField(auto_now=True)
    datetime_to_start_show = models.DateTimeField()
    datetime_to_last_update = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(SectionNews, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tiny_image = models.ImageField('Маленькая картинка', upload_to=get_path_to_tiny_image)

    def __str__(self):
        return self.title

#    def save(self, *args, **kwargs):
#        self.title = 'NEWS TITLE SAVE'
#        o = News.objects.all()
#        list_o = []
#        for i in o:
#            list_o.append(i.id)
#        self.id = 1
#        while True:
#            if self.id in list_o:
#                self.id += 1
#            break
#        super(News, self).save(*args, **kwargs)

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-datetime_to_start_show']


class NewsCounter(models.Model):
    count = models.IntegerField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.count} {self.news.title}'

    class Meta:
        db_table = 'newscounter'
        verbose_name = 'Счетчик новостей'
        verbose_name_plural = 'Счетчик новостей'


class CommentNews(models.Model):
    text = models.CharField(max_length=450)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    datetime_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner.username} {self.news.title}'

    class Meta:
        db_table = 'commentnews'
        verbose_name = 'Комментарий к новости'
        verbose_name_plural = 'Комментарии к новостям'
