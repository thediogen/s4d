# from django.contrib import admin
from django.urls import path, include

# from shop import market
from .views import index, about_us, register


urlpatterns = [
    path('', index, name='index'),
    path('aboutus', about_us, name='aboutus'),
    path('register', register, name='register')
]
