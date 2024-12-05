# from django.core.management.base import BaseCommand
# from catalog.models import Product, Category
#
# class Command(BaseCommand):
#     help = 'Добавьте тестовые продукты'
#
#     def handle(self, *args, **kwargs):
#         if kwargs['delete']:
#             Product.objects.all().delete()
#             Category.objects.all().delete()
#
#
#         electronics = Category.objects.create(name='Electronics', slug='electronics')
#         books = Category.objects.create(name='Books', slug='books')
#
#
#         Product.objects.create(title='Smartphone', description='Latest model smartphone.', price=699.99, category=electronics)
#         Product.objects.create(title='Laptop', description='High performance laptop.', price=999.99, category=electronics)
#         Product.objects.create(title='Python Programming Book', description='A comprehensive guide to Python programming.', price=29.99, category=books)
#         Product.objects.create(title='Django for Beginners', description='Learn Django from scratch.', price=39.99, category=books)
#
#         self.stdout.write(self.style.SUCCESS('Successfully added test products'))
#
#
#
# #
# from django.core.management.base import BaseCommand
# from catalog.models import Product, Category
#
# class Command(BaseCommand):
#     help = 'Add test products to the category'
#
#     def handle(self, *args, **kwargs):
#         category, _ = Category.objects.get_or_create(name = 'Tableware')
#
#         products = [
#             {'name': 'spoons'},
#         ]
#
#         for products_data in products:
#             product, created = Product.objects.get_or_create(**products_data)
#             if created:
#                 self.stdout.write(self.style.SUCCESS(f'Successfully added : {product.title}'))
#             else:
#                 self.stdout.write(self.style.WARNING(f'It already exists: {product.title}'))
import os

from django.core.management.base import BaseCommand

from catalog.models import Product, Category
#
# class Command(BaseCommand):
#     help = 'Add test products to the category'
#
#     def handle(self, *args, **kwargs):
#         category, _ = Category.objects.get_or_create(name='Tableware')
#
#         products = [
#             {'name': 'spoons'},
#         ]
#
#         for products_data in products:
#             product, created = Product.objects.get_or_create(**products_data)
#             if created:
#                 self.stdout.write(self.style.SUCCESS(f'Successfully added : {product.title}'))
#             else:
#                 self.stdout.write(self.style.WARNING(f'It already exists: {product.title}'))

from django.db import connection

from catalog.util import read_JSON_data

category_file_path = os.path.join(
    "category_data.json"
)
products_file_path = os.path.join(
    "product_data.json"
)

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.clean_database()
        self.reset_sequences()
        self.load_categories()
        self.load_products()

    def clean_database(self):
        """Очищаем базу данных"""
        Product.objects.all().delete()
        Category.objects.all().delete()

    def reset_sequences(self):
        """Сбрасываем автоинкрементные значения таблиц"""
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")

    def load_categories(self):
        """Загружаем в БД данные по категориям"""
        category_list = read_JSON_data(category_file_path)
        for category_item in category_list:
            category_fields = category_item["fields"]
            Category.objects.create(**category_fields)

    def load_products(self):
        """Загружаем в БД данные по продуктам"""
        product_list = read_JSON_data(products_file_path)
        for product_item in product_list:
            product_fields = product_item["fields"]
            category_id = product_fields.pop("category")
            Product.objects.create(category_id=category_id, **product_fields)


