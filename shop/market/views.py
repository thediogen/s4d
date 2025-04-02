from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.


def index(request):

    context = {
        'title': 'GoIteens Shop'
    }

    return render(request, 'index.html', context=context)


def about_us(request):
    context = {
        'title': 'About Us'
    }

    return render(request, 'aboutUs.html', context=context)


# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful")
#             return redirect('index')
#         else:
#             return render(request, '400.html')

#     form = NewUserForm()
#     return render(request=request, template_name="register.html", context={"register_form": form})
