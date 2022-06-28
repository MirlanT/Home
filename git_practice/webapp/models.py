from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    content = models.TextField(max_length=350, null=False, blank=False, verbose_name='Контент')
    author = models.CharField(max_length=20, null=False, blank=False, default='Unknown', verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Создание времени")
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title, self.content)
