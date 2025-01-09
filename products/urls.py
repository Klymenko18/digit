from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView
from django.views.generic import TemplateView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),


    # Frontend Templates
    path('categories/', TemplateView.as_view(template_name='category_list.html'), name='category-list-template'),
    path('categories/create/', TemplateView.as_view(template_name='category_form.html'), name='category-create-template'),
    path('categories/<int:pk>/edit/', TemplateView.as_view(template_name='category_form.html'), name='category-edit-template'),

    path('products/', TemplateView.as_view(template_name='product_list.html'), name='product-list-template'),
    path('products/create/', TemplateView.as_view(template_name='product_form.html'), name='product-create-template'),
    path('products/<int:pk>/edit/', TemplateView.as_view(template_name='product_form.html'), name='product-edit-template'),
]
