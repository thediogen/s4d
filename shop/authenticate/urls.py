from django.urls import path, include

from .views import CustomLoginView, register


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', register, name='register')
]
