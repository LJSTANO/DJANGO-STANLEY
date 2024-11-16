from django.db import models

# Create your models here.
class Product (models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_exp = models.DateField()
    prod_quantity = models.IntegerField()
    prod_manufacture = models.DateField()
    prod_description = models.CharField(max_length=100)
    prod_img = models.ImageField(upload_to='products/')

# class Team (models.Model):