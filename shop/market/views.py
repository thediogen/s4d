import traceback

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import Person

def index(request):

    context = {
        "title": "TEST TITLE"
    }

    return render(request, 'index.html', context)


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