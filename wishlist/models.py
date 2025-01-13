from django.db import models
from django.contrib.auth.models import User
from products.models import Product  # Має бути модель продуктів

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Зв'язок з користувачем
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Зв'язок з продуктом
    added_at = models.DateTimeField(auto_now_add=True)  # Коли товар додано

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
