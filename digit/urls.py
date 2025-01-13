from django.contrib import admin
from django.urls import include, path
from products.views import product_list
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cart/', include('cart.urls')),  # API кошика
    path('products/', product_list, name='product-list'),  # Перелік продуктів
    path('cart/', TemplateView.as_view(template_name="cart.html"), name='cart'),  # Сторінка кошика
    path('', TemplateView.as_view(template_name="index.html"), name='home'),  # Головна сторінка
    path('orders/', include('orders.urls')),  # Замовлення
    path('accounts/', include('accounts.urls')),  # Акаунти
]
