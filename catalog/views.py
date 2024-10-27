from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Product


# Create your views here.
def show_home(request: HttpRequest):
    """функция обрабатывает запрос и возвращает html-страницу"""
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'products': products}

        return render(request, "catalog/home.html", context=context)


def contacts(request: HttpRequest):
    """Обрабатываем форму и возвращаем ответ"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')


def product_detail(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context=context)
