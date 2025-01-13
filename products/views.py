from rest_framework import generics
from django.shortcuts import render
from django.core.cache import cache
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.views.decorators.cache import cache_page

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        # Отримуємо список категорій з кешу або бази
        cache_key = 'category_list'
        categories = cache.get(cache_key)

        if not categories:
            categories = list(Category.objects.all())
            cache.set(cache_key, categories, timeout=600)  # 10 хвилин

        search_query = request.GET.get('search', '')
        if search_query:
            categories = [category for category in categories if search_query.lower() in category.name.lower()]

        return render(request, 'categories.html', {'categories': categories})

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def product_list(request):
    # Отримуємо список продуктів з кешу
    products = cache.get('product_list')
    
    if not products:
        products = Product.objects.all()
        cache.set('product_list', products, timeout=60)
    
    search_query = request.GET.get('search', '')
    if search_query:
        products = [product for product in products if search_query.lower() in product.name.lower()]

    return render(request, 'products.html', {'products': products})

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
