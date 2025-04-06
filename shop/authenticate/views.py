from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

from .forms import AuthenticationForm, RegistrationForm

# Create your views here.


class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'login.html'


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')

    form = RegistrationForm()
    return render(request, 'register.html', context={ 'form': form })
