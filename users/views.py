from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User as CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .forms import RegisterForm
from django.core.mail import send_mail

class RegisterView(APIView):
    def post(self, request):
        form = RegisterForm(request.data)
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
            return Response({'message': 'Пользователь создан'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
