from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User as CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import RegisterForm, CustomAuthenticationForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# class RegisterView(APIView):
#     def post(self, request):
#         form = RegisterForm(request.data)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             send_mail(
#                 'Приветствие',
#                 'Добро пожаловать на наш сайт!',
#                 'your_email@example.com',
#                 [user.email],
#                 fail_silently=False,
#             )
#             return Response({'message': 'Пользователь создан'}, status=status.HTTP_201_CREATED)
#         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            send_mail(
                'Приветствие',
                'Добро пожаловать на наш сайт!',
                'your_email@example.com',
                [user.email],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


