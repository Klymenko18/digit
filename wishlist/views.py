from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]  # Доступ тільки для авторизованих користувачів

    def get_queryset(self):
        """Повертає тільки список бажань для поточного користувача"""
        return Wishlist.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_to_wishlist(self, request, pk=None):
        """Додає товар в список бажань"""
        product = Product.objects.get(id=pk)
        wishlist_item = Wishlist.objects.create(user=request.user, product=product)
        return Response({"status": "Product added to wishlist", "item": WishlistSerializer(wishlist_item).data})
