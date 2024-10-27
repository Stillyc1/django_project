from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Article


class ArticleCreateView(CreateView):
    """контроллер Создание статьи"""
    model = Article
    template_name = "blogs/create_article.html"
    context_object_name = "article_create"

    fields = ('header', 'content')
    success_url = reverse_lazy('blogs:article_list')


class ArticleListView(ListView):
    """Контроллер получения списка всех статей"""
    model = Article
    template_name = "blogs/article_list.html"
    context_object_name = "article_list"


class ArticleUpdateView(UpdateView):
    """Контроллер изменения статьи"""
    model = Article
    template_name = "blogs/article_update.html"
    context_object_name = "article_update"


class ArticleDeleteView(DeleteView):
    """Контроллер удаления статьи"""
    model = Article
    context_object_name = "article_delete"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blogs/article_detail.html"
    context_object_name = "article_detail"
