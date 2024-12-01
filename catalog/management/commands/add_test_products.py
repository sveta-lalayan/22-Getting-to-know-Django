from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавьте тестовые продукты'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()


        electronics = Category.objects.create(name='Electronics', slug='electronics')
        books = Category.objects.create(name='Books', slug='books')


        Product.objects.create(title='Smartphone', description='Latest model smartphone.', price=699.99, category=electronics)
        Product.objects.create(title='Laptop', description='High performance laptop.', price=999.99, category=electronics)
        Product.objects.create(title='Python Programming Book', description='A comprehensive guide to Python programming.', price=29.99, category=books)
        Product.objects.create(title='Django for Beginners', description='Learn Django from scratch.', price=39.99, category=books)

        self.stdout.write(self.style.SUCCESS('Successfully added test products'))




