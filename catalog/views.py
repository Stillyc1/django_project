from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def show_home(request: HttpRequest):
    """функция обрабатывает запрос и возвращает html-страницу"""
    return render(request, "catalog/home.html")
