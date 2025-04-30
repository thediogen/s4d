from django.contrib import admin

# Register your models here.


from .models import Person, Musician, Album, Stuff


@admin.register(Person, Musician, Album, Stuff)
class Market(admin.ModelAdmin):
    ...
