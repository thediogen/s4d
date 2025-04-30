import traceback

from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from .models import Person

def index(request):

    context = {
        "title": "test title"
    }

    return render(request, 'index.html', context)


def about_us(request):
     context = {
         'title': 'About Us'
     }
 
     return render(request, 'aboutUs.html', context=context)


def get_person_by_pk(request, pk: int):
    try:
        person = Person.objects.get(pk=pk)
        return HttpResponse(f"{person}")
    except ObjectDoesNotExist:
        return HttpResponse(f"error: Person with {pk} does not exists")

def get_person_by_surname(request, surname: str):
    person = Person.objects.get(last_name=surname)
    return HttpResponse(f"{person}")


def get_or_create_person(request, pk:int):
    person = Person.objects.get_or_create(
        pk=pk,
        defaults={
            "first_name": "John",
            "last_name": "Sina"
        }
    )

    return HttpResponse(f"{person}")


def change_surname(request, pk: int, surname: str):
    try:
        person = Person.objects.get(pk=pk)

        person.last_name = surname
        person.save()

        return HttpResponse(f"New surname for user - {person.first_name}, {person.last_name}")

    except ObjectDoesNotExist:
        return HttpResponseBadRequest(
            {
                "error": f"Person with {pk} does not exists",
                "traceback": traceback.format_exc()
            }
        )


def create_person(request):
    p = Person(first_name="Patrick", last_name="Saint")

    p.save()
    return HttpResponse("Created")


def update_or_create_person(request, name:str):
    person = Person.objects.update_or_create(
        first_name=name,
        defaults={
            "first_name": "Oguzik",
            "last_name": "Lavrov"
        }
    )
    return HttpResponse(f"{person}")


def delete_person(request, pk: int):
    person = Person.objects.get(
        pk=pk,
    )
    person.delete()
    return HttpResponse(f"Deleted person")

def get_all_persons(request):
    persons = Person.objects.all()
    for person in persons:
        print(person)

    return render(request, "persons.html", context={"persons": persons})


def request_info_check(request):
    info = []

    # Основні атрибути
    info.append(f"Method: {request.method}")
    info.append(f"Scheme: {request.scheme}")
    info.append(f"Path: {request.path}")
    info.append(f"Encoding: {request.encoding}")
    info.append(f"Content-Type: {request.content_type}")
    info.append(f"Content Params: {request.content_params}")
    # GET і POST параметри
    info.append(f"GET params: {dict(request.GET)}")
    info.append(f"POST params: {dict(request.POST)}")

    # Файли
    info.append(f"FILES: {[f.name for f in request.FILES.values()]}")

    # META-поля (тільки кілька, бо їх дуже багато)
    meta_keys = [
        'CONTENT_LENGTH', 'CONTENT_TYPE', 'HTTP_USER_AGENT',
        'HTTP_ACCEPT', 'HTTP_HOST', 'HTTP_REFERER',
        'REMOTE_ADDR', 'REMOTE_HOST', 'REMOTE_USER',
        'QUERY_STRING', 'SERVER_NAME', 'REQUEST_METHOD'
    ]
    for key in meta_keys:
        info.append(f"META[{key}]: {request.META.get(key)}")

    # resolver_match
    info.append(f"Resolver match: {request.resolver_match}")

    # Заголовки (Django 2.2+)
    if hasattr(request, 'headers'):
        headers = '\n'.join([f"{k}: {v}" for k, v in request.headers.items()])
        info.append("Headers:\n" + headers)

    # Додаткові методи
    info.append(f"Host: {request.get_host()}")
    info.append(f"Port: {request.get_port()}")
    info.append(f"Full Path: {request.get_full_path()}")
    info.append(f"Absolute URL: {request.build_absolute_uri()}")
    info.append(f"Is secure: {request.is_secure()}")

    # AJAX-перевірка
    if hasattr(request, 'is_ajax'):  # Застаріле, але покажемо
        info.append(f"Is AJAX: {request.is_ajax()}")

    return HttpResponse("<br>".join(info), content_type="text/html")


@require_http_methods('')
def tutorial(request):
    return HttpResponseRedirect(reverse('check'))



class About(TemplateView):
    template_name = 'about.html'


# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful")
#             return redirect("index")
#         else:
#             return render(request, '400.html')
#
#     form = NewUserForm()
#     return render(request=request, template_name="register.html", context={"register_form": form})