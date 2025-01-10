from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
      name = models.CharField(max_length=50)
      description = models.CharField(blank=True,null=True)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      image = models.ImageField(upload_to='products/', blank=True, null=True)
      category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
      stock_quantity = models.IntegerField(default=0)