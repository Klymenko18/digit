from django.urls import path
from .views import RegisterAPIView, LoginAPIView, login_page, register_page, register_success
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api-register'),  # API для реєстрації
    path('register-page/', register_page, name='register-page'),  # Сторінка реєстрації
    path('register-success/', register_success, name='register-success'),
    path('login/', LoginAPIView.as_view(), name='api-login'),  # API для логіну
    path('login-page/', login_page, name='login-page'),  # Сторінка логіну
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
