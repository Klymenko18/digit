from django.contrib import admin
from django.urls import include, path
from products.views import product_list, CategoryProductsView
from django.views.generic import TemplateView
from .views import home  # Імпорт вашої функції home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cart/', include('cart.urls')),
    path('products/', product_list, name='product-list'),
    path('cart/', TemplateView.as_view(template_name="cart.html"), name='cart'),
    path('', home, name='home'),  # Замінили TemplateView на вашу функцію home
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/template/', TemplateView.as_view(template_name='categories.html'), name='category-list-template'),
    path('categories/<int:category_id>/products/', CategoryProductsView.as_view(), name='category-products'),
    path('wishlist/', include('wishlist.urls')),
]
