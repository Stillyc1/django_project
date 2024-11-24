from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm, ProductModerForm
from .models import Product, Category
from users.models import CustomUser
from .services import GetListProduct, LoadProductCategory


# Create your views here.
class CatalogListView(ListView):
    """Класс представления каталога товаров на главной странице"""
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        return GetListProduct.get_list_product_from_cache()


class ProductCategoryView(ListView):
    """Класс представления категории продуктов"""
    model = Product
    template_name = "catalog/product_category.html"
    context_object_name = 'product_category'

    def get_queryset(self):
        return LoadProductCategory.load_product_category(category_id=self.kwargs.get('pk'))


@method_decorator(cache_page(60), name='dispatch')
class CatalogDetailView(DetailView):
    """Класс представления полной информации о товаре, на отдельной странице"""
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class CatalogCreateView(LoginRequiredMixin, CreateView):
    """контроллер Создание продукта"""
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm
    success_url = reverse_lazy('catalog:show_home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения продукта"""
    model = Product
    template_name = "catalog/product_create.html"
    context_object_name = "product_create"

    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        """
        Проверка чтобы пользователь был владельцем продукта и тогда может его изменять
        и если у пользовтаеля есть право can_unpublish_product
        """
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModerForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления продукта"""
    model = Product
    context_object_name = "product_delete"

    success_url = reverse_lazy("catalog:show_home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.delete_product'):
            return super().get_form_class()
        raise PermissionDenied


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
