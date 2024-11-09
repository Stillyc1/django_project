from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Product


# Create your views here.
class CatalogListView(ListView):
    """Класс представления каталога товаров на главной странице"""
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CatalogDetailView(DetailView):
    """Класс представления полной информации о товаре, на отдельной странице"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class CatalogCreateView(CreateView):
    """контроллер Создание статьи"""
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm
    success_url = reverse_lazy('catalog:show_home')


class ProductUpdateView(UpdateView):
    """Контроллер изменения продукта"""
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    """Контроллер удаления продукта"""
    model = Product
    context_object_name = "product_delete"

    success_url = reverse_lazy("catalog:show_home")


class CatalogTemplateView(TemplateView):
    """Класс представления обратной связи с заполнением формы"""
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        """Обрабатываем форму и возвращаем ответ"""
        if self.request.method == 'POST':
            # Получение данных из формы
            name = request.POST.get('name')
            message = request.POST.get('message')
            # Обработка данных (например, сохранение в БД, отправка email и т. д.)
            # Здесь мы просто возвращаем простой ответ
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
        return render(request, 'catalog/contacts.html')
