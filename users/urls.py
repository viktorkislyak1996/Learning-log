from django.urls import path, include
from . import views


"""Определяет схемы URL для пользователей"""
app_name = 'users'
urlpatterns = [
    # Включить URL аутентификации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации пользователей
    path('register/', views.register, name='register'),

]