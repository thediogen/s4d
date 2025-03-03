# from django.contrib import admin
from django.urls import path, include

# from shop import market
from .views import index


urlpatterns = [
    path('', index, name='index')
]
