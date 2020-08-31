from django.db import models


# Create your models here.
class Product(models.Model):
    prod_no = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    prod_price = models.FloatField()
    prod_qty = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


