from rest_framework import viewsets
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def wishlist_page(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist': wishlist_items})

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_to_wishlist(self, request, pk=None):
        try:
            product = Product.objects.get(id=pk)
            wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
            if not created:
                return Response({"status": "Product already in wishlist"})
            return Response({"status": "Product added to wishlist", "item": WishlistSerializer(wishlist_item).data})
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=404)

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"'{product.name}' was added to your wishlist.")
    else:
        messages.info(request, f"'{product.name}' is already in your wishlist.")
    return redirect('wishlist-page')

@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    item.delete()
    messages.success(request, "Item was removed from your wishlist.")
    return redirect('wishlist-page')