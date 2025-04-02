from django.urls import path, include

from .views import create_get_form

urlpatterns = [
    path('', create_get_form)
]
