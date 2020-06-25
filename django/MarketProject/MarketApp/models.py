from django.db import models

# Create your models here.

class Markets(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    market = models.ForeignKey(Markets, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class History_Carts(models.Model):
    idCart = models.IntegerField()
    nameProduct = models.CharField(max_length=30)
    nameMarket = models.CharField(max_length=50)
    priceProduct = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)