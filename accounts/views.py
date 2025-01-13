from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .serializers import UserSerializer
from django.http import HttpResponseRedirect

class RegisterAPIView(APIView):
    permission_classes = []  # Дозволяємо реєстрацію без авторизації

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect('/accounts/register-success/')  # Перенаправлення після успіху
        return render(request, 'register.html', {'form': serializer, 'errors': serializer.errors})

class LoginAPIView(APIView):
    permission_classes = []  # Логін без авторизації

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')  # Перенаправлення на головну сторінку після успішного входу
        else:
            messages.error(request, 'Invalid username or password')  # Повідомлення про помилку
            return redirect('login-page')  # Перенаправлення назад на сторінку логіну
def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "User registered successfully!")
            return redirect("register-page")  # Повернення на сторінку реєстрації

    return render(request, "register.html")

def register_success(request):
    return render(request, 'register_success.html')
