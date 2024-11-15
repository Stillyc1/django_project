from django.urls import path

from .views import CatalogListView, CatalogDetailView, CatalogTemplateView, CatalogCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'


urlpatterns = [
    path('', CatalogListView.as_view(), name='show_home'),
    path('contacts/', CatalogTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>', CatalogDetailView.as_view(), name='product'),
    path('add_product/', CatalogCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
