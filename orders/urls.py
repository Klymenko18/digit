from django.urls import path
from django.views.generic import TemplateView
from .views import OrderListView, OrderDetailView

urlpatterns = [
    # Головна сторінка
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    
    # Створення нового замовлення (форма)
    path('orders/new/', TemplateView.as_view(template_name="order_form.html"), name='order-form'),
    
    # Історія замовлень
    path('orders/history/', TemplateView.as_view(template_name="order_history.html"), name='order-history'),
    
    # API для замовлень
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
]
