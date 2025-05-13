from rest_framework import serializers
from .models import CartItem, Cart
from products.models import Product
from products.serializers import ProductSerializer  # Імпортуємо серіалізатор продукту

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Вкладена інформація про продукт

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)  # Вкладена інформація про товари

    class Meta:
        model = Cart
        fields = ['id', 'cart_items', 'created_at']
