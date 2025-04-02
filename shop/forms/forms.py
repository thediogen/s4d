from django.forms import Form, CharField, TextInput, Textarea, ModelForm

from .models import Article


class ArticleForms(ModelForm):
    class Meta:
        model = Article
        exclude = []
