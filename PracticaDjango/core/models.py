from django.db import models

# Create your models here.

class Cliente(models.Model):
    rutcliente = models.CharField(primary_key=True,max_length=10, verbose_name='rut del cliente')
    nombre = models.CharField(max_length=50, verbose_name='nombre completo del cliente')
    correo = models.CharField(max_length=50, verbose_name='correo del cliente')
    telefono = models.IntegerField(verbose_name='telefono del cliente')
    direccion = models.CharField(max_length=50, verbose_name='direccion del cliente')

    def __str__(self):
        return self.rutcliente

class Producto(models.Model):
    codigo= models.IntegerField(primary_key=True, max_length=6, verbose_name='codigo')
    nombre= models.CharField(max_length=50, verbose_name='nombre')
    precio= models.IntegerField(verbose_name='precio')
    stock =models.IntegerField(verbose_name='stock', null=True)
    descripcion = models.CharField(max_length=100, verbose_name='descripcion')

    def __str__(self):
        return self.codigo