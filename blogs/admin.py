from django.contrib import admin

from blogs.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Отображает модели(таблицу) Статей в админке"""
    list_display = ('id', 'header', 'created_at', 'updated_at', 'is_active', 'number_of_views',)
    list_filter = ('header', 'created_at', 'is_active',)
    search_fields = ('id', 'header', 'created_at', 'updated_at', 'is_active', 'number_of_views',)
