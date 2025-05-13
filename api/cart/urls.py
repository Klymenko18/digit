from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='cart-add'),
    path('remove/', RemoveFromCartView.as_view(), name='cart-remove'),
]
