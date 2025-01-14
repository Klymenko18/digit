from django.contrib import admin
from django.urls import include, path
from products.views import product_list
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cart/', include('cart.urls')),
    path('products/', product_list, name='product-list'),
    path('cart/', TemplateView.as_view(template_name="cart.html"), name='cart'),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/template/', TemplateView.as_view(template_name='categories.html'), name='category-list-template'),
    path('wishlist/', include('wishlist.urls')),   
]
