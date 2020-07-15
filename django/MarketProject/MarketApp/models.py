from django.db import models

# Create your models here.

class Markets(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='markets')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'market'
        verbose_name_plural = 'markets'
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    price = models.FloatField()
    market = models.ForeignKey(Markets, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='products')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return self.name, self.market.name

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'cart'

class History_Carts(models.Model):
    idCart = models.IntegerField()
    nameProduct = models.CharField(max_length=30)
    nameMarket = models.CharField(max_length=50)
    priceProduct = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'history_cart'
        verbose_name_plural = 'history_carts'