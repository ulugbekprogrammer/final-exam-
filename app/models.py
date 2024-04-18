from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)