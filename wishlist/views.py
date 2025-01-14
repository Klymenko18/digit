from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product  # Додано імпорт для моделі Product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def wishlist_page(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist_items})


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Повертає тільки список бажань для поточного користувача"""
        return Wishlist.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_to_wishlist(self, request, pk=None):
        """Додає товар в список бажань"""
        try:
            product = Product.objects.get(id=pk)
            wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
            if not created:
                return Response({"status": "Product already in wishlist"})
            return Response({"status": "Product added to wishlist", "item": WishlistSerializer(wishlist_item).data})
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=404)
