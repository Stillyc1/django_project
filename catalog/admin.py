from django.contrib import admin
from .models import Category, Product

# создали админку python manage.py createsuperuser
# создали классы для отображения моделей в админке


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Категории в админке"""
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Продуктов в админке"""
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('name', 'price', 'category',)
    search_fields = ('id', 'name', 'category__name',)
