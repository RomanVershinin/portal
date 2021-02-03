from django.db import models

# Create your models here.


from django.contrib.auth.models import User


class Podrazdelenie(models.Model):
    title = models.CharField('Название подразделения', max_length=150)
    unicum_id = models.IntegerField()

    def _str__(self):
        return self.title

    class Meta:
        db_table = 'podrazdelenie'
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class MyLocalUser(User):
    podrazdelenie = models.ForeignKey(Podrazdelenie, on_delete=models.CASCADE)
    index_sortirovki = models.IntegerField('Индекс сортировки', blank=True, null=True)
    position = models.CharField('Должность в организации', max_length=150)


    def __str__(self):
        return f'{self.username}'

    class Meta:
        db_table = 'mylocaluser'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
