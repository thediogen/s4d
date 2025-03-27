from django.db import models

from market.enums.cart_status import CartStatus

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Cart(models.Model):
    
    # поле cart_items зробив через CharField бо в sqlite 
    # (по крайній мірі в django ORM) немає типу для списків
    cart_items = models.CharField(max_length=256)
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    status = models.CharField(choices=CartStatus.choices(), max_length=len(CartStatus.waiting_for_accept.value))
