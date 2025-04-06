from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class CustomAuthForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    
    def clean(self):
        # super(CustomAuthForm, self).clean()
        email = self.cleaned_data.get('email')

        if email:
            self.user_cache = authenticate(
                self.request,
                username=email,
                password=self.cleaned_data.get('password')
            )

            if self.user_cache is None:
                raise forms.ValidationError('User cache is none')
        
        return self.cleaned_data


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

