from django.urls import path

from .views import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = 'blogs'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('add_article/', ArticleCreateView.as_view(), name='article_create'),
    path('blog/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete')
]
