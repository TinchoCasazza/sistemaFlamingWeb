# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre =  models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Documento = models.CharField(max_length=12)

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Detalle = models.CharField(max_length=50, blank= True, null = True)
    Cantidad = models.IntegerField(blank= True, null = True)
    PrecioVenta = models.DecimalField(max_digits=7, decimal_places=2)
    PrecioCosto = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.Nombre

class TipoPago(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=20)

#class DetalleCompra(models.Model):    

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']
