from django.db import models

class Blog(models.Model):
    slug = models.CharField(max_length=100, verbose_name='slug', blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(verbose_name='Изображение',blank=True, null=True)
    count_views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    date_publications = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    is_publication = models.BooleanField(default=True, verbose_name='Признак публикации')



    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
