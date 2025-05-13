from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product, Category

class ProductSearchFilterTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        Product.objects.create(name='Smartphone', category=self.category, price=500)
        Product.objects.create(name='Laptop', category=self.category, price=1000)

    def test_search_by_name(self):
        response = self.client.get('/api/products/', {'search': 'Smartphone'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_category(self):
        response = self.client.get('/api/products/', {'category': 'Electronics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_price(self):
        response = self.client.get('/api/products/', {'min_price': 600})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
