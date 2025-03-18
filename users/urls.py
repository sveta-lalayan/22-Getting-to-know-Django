from django.urls import path
from .views import RegisterForm, login_view

urlpatterns = [
    path('register/', RegisterForm, name='register'),
    path('login/', login_view, name='login'),
]