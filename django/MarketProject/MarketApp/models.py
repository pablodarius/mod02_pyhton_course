from django.db import models

# Create your models here.

class Markets(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    market = models.ForeignKey(Markets, on_delete=models.CASCADE)