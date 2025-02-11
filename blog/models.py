# from django.db import models
#
# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     preview_image = models.ImageField(upload_to='images/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_published = models.BooleanField(default=False)
#     views_count = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.title



from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/image', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publication = models.BooleanField(default=True, verbose_name='публикация')
    number_views = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
