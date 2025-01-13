from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class OrderListView(APIView):
    """
    Отримати список замовлень або створити нове замовлення.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        products_data = data.get('products', [])
        total_price = 0

        # Створити нове замовлення
        order = Order.objects.create(
            user=user,
            delivery_address=data.get('delivery_address', ''),
            total_price=0  # Обчислимо пізніше
        )

        for product_data in products_data:
            try:
                product = Product.objects.get(id=product_data['product_id'])
                quantity = product_data['quantity']
                price = product.price * quantity

                # Додати продукт до OrderItem
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )

                total_price += price
            except Product.DoesNotExist:
                return Response({"error": f"Product with id {product_data['product_id']} does not exist"},
                                status=status.HTTP_400_BAD_REQUEST)

        # Оновити загальну ціну
        order.total_price = total_price
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    """
    Отримати або видалити окреме замовлення.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            order.delete()
            return Response({"message": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
