from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """контроллер Создание статьи"""
    model = Article
    template_name = "blogs/create_article.html"
    context_object_name = "article_create"

    fields = ('header', 'content', 'picture',)
    success_url = reverse_lazy('blogs:article_list')


class ArticleListView(ListView):
    """Контроллер получения списка всех статей"""
    model = Article
    template_name = "blogs/article_list.html"
    context_object_name = "article_list"

    def get_queryset(self):
        return Article.objects.filter(is_active=True)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменения статьи"""
    model = Article
    template_name = "blogs/create_article.html"
    context_object_name = "article_create"

    fields = ('header', 'content', 'picture',)

    def get_success_url(self):
        return reverse('blogs:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления статьи"""
    model = Article
    context_object_name = "article_delete"

    success_url = reverse_lazy("blogs:article_list")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blogs/article_detail.html"
    context_object_name = "article_detail"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()

        return self.object
