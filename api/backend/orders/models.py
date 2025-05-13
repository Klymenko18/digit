from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")  # Зв'язок з користувачем
    products = models.ManyToManyField(Product, through="OrderItem", related_name="orders")  # Зв'язок з товарами
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  
    delivery_address = models.CharField(max_length=255)  
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Статус замовлення
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items") 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")  
    quantity = models.PositiveIntegerField(default=1)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"