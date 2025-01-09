from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),  

    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('categories/', TemplateView.as_view(template_name="categories.html"), name='categories'),
    path('categories/<int:pk>/', TemplateView.as_view(template_name="category_detail.html"), name='category-detail'),
    path('products/', TemplateView.as_view(template_name="products.html"), name='products'),
    path('products/create/', TemplateView.as_view(template_name="product_form.html"), name='product-create'),
    path('products/<int:pk>/', TemplateView.as_view(template_name="product_detail.html"), name='product-detail'),
    path('products/<int:pk>/edit/', TemplateView.as_view(template_name="product_form.html"), name='product-edit'),
]
