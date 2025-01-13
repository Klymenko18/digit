from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')  # Додаткове поле для назви продукту

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Вкладений серіалізатор для елементів замовлення
    user = serializers.ReadOnlyField(source='user.username')  # Ім'я користувача

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'delivery_address', 'order_status', 'created_at', 'updated_at']
