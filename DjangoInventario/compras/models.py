# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.

class DetalleCompra():
    def __init__(self):
        self.FechaCarga = null
        self.Precio = null

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre =  models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    CUIT = models.CharField(max_length=12)
    Direccion = models.CharField(max_length =40)

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Cantidad = models.IntegerField(blank= True, null = True, default = 0)
    PrecioVenta = models.DecimalField(max_digits=7, decimal_places=2)
    PrecioCosto = models.DecimalField(max_digits=7, decimal_places=2)
    objects = models.Manager()

    def __str__(self):
        return self.Nombre

    def calcularGanancia(self):
        return ( self.PrecioVenta - self.PrecioCosto )
    
    def save(self, **kwargs):
        super(Producto, self).save(**kwargs)
        compra = ModelCompra(producto=self)
        compra.save()

class TipoPago(models.Model):
    id = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=20)

class ModelCompra(models.Model):
    idCompra = models.AutoField(primary_key = True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    Compras = models.IntegerField(default=0)
    ExistenciaFinal = models.IntegerField(default=0)
    CostoUnidades = models.IntegerField(default=0)
    Precio = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    Costo = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    objects = models.Manager()


