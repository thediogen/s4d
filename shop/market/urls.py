from django.urls import path

from .views import (index, get_person_by_pk, get_person_by_surname, change_surname, get_or_create_person,
                    update_or_create_person, create_person, delete_person, get_all_persons, request_info_check,
                    tutorial, about_us)

urlpatterns = [
    path("", index, name="index"),
    path("get/<int:pk>", get_person_by_pk),
    path("get/<str:surname>", get_person_by_surname),
    path("get_or_create_person/<int:pk>", get_or_create_person),
    path("change_surname/<int:pk>/<str:surname>", change_surname),
    path("update/<str:name>", update_or_create_person),
    path("create", create_person),
    path("delete/<int:pk>", delete_person),
    path("all", get_all_persons),
    path('check', request_info_check, name='check'),
    # path('v2', ),
    path('reverse', tutorial),
    path('aboutus', about_us)
]
