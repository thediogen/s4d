from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Child(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(default=1)
    tags = ArrayField(models.CharField(max_length=100))
    email = models.EmailField(unique=True)
    fav_toy = models.CharField(max_length=64, blank=True, default='')


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    email = models.EmailField(max_length=254)
    url_image = models.URLField(max_length=200)
    is_discount = models.BooleanField(default=False)
    price = models.IntegerField()
    price_2 = models.PositiveSmallIntegerField()

    created_at = models
    expiration = models.TimeField()
