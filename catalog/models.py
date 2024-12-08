
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование категории', help_text='Введите наименование категории')
    description = models.CharField(max_length=150, verbose_name='описание категории', help_text='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', 'description']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование', help_text='Введите наименование')
    description = models.CharField(max_length=150, verbose_name='описание', help_text='Введите описание')
    image = models.ImageField(upload_to='catalog/images', blank=True, null=True, verbose_name='изображение', help_text='Добавьте фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', help_text='Выберите категорию')
    price = models.CharField(max_length=150, verbose_name='цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания', help_text='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения', help_text='Дата изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description']

    def __str__(self):
        return self.name
