from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=500, verbose_name='La Dirección')
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField("El teléfono", max_length=7, blank=True, null=True) # el verbose name no funcionaria para FK
    
    def __str__(self):
        return 'El nombre es %s, con dirección %s, email %s y teléfono %s' % (self.nombre, self.direccion, self.email, self.telefono)


class articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()