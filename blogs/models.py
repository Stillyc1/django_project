from django.db import models


# Create your models here.
class Article(models.Model):
    """Модель создания статьи в блоге"""
    objects = None
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    picture = models.ImageField(upload_to='blogs/photo/', verbose_name='Изображение', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    number_of_views = models.IntegerField(default=0)

    def __str__(self):
        return f"Статья - {self.header}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
