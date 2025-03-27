from django.contrib import admin

# Register your models here.


from .models import Person, Musician, Album


@admin.register(Person, Musician, Album)
class Market(admin.ModelAdmin):
    ...
