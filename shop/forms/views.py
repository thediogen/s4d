from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

from .forms import ArticleForms
from .models import Article

# Create your views here.


def create_get_form(request: HttpRequest):
    if request.method == 'POST':
        form = ArticleForms(request.POST)

        if form.is_valid():
            new_article = Article(
                title=form.cleaned_data['title'], 
                body=form.cleaned_data['body']
            )
            new_article.save()

            return HttpResponse('Tnx for a new article')
        
    context = {}
    form = ArticleForms()
    context['form'] = form

    return render(request, 'form.html', context=context)
