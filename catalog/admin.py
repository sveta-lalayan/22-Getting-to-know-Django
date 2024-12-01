from django.contrib import admin
from.models import Category,Product
#
#
# admin.site.register (Category)
# admin.site.register (Product)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Отображаем id и name в списке категорий

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Отображаем id, name, price и category в списке продуктов
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description')  # Поиск по полям name и description

# Регистрация моделей с настройками админки
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
