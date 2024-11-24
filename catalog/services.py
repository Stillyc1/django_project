from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Product


class LoadProductCategory:
    """Класс обработки Категорий продуктов"""
    @staticmethod
    def load_product_category(category_id):
        """Метод получает данные о продукатх определенной категории"""
        product_category = Product.objects.filter(category=category_id)
        return product_category


class GetListProduct:
    """Класс обработки получения списка продуктов"""
    @staticmethod
    def get_list_product_from_cache():
        """Метод получает данные от БД, если списка продуктов нет в кэше, то добавляет его и возвращает список"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'product_list'
        products = cache.get(key)

        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products
