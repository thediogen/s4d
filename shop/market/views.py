from django.shortcuts import render

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
