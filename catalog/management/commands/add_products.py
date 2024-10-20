from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем всю инфу из БД
        Category.objects.all().delete()
        Product.objects.all().delete()

        # наполняем таблицу категории данными о категории
        category, _ = Category.objects.get_or_create(name='Что-то там', description='Реально что-то там')

        # Продукты категории
        products = [
            {'name': 'Кто-то', 'description': 'Кто-то есть', 'category': category, 'price': 50},
            {'name': 'Куда-то', 'description': 'Куда-то есть', 'category': category, 'price': 100},
        ]

        # циклом выполняем команду заполнения таблицу продуктов данными
        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
