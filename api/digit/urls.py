from django.contrib import admin
from django.urls import include, path
from products.views import product_list, CategoryProductsView
from django.views.generic import TemplateView
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('products/', product_list, name='product-list'),
    path('', home, name='home'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
    path('categories/template/', TemplateView.as_view(template_name='categories.html'), name='category-list-template'),
    path('categories/<int:category_id>/products/', CategoryProductsView.as_view(), name='category-products'),
    path('wishlist/', include('wishlist.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
