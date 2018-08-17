from django.db import models
from django.utils import timezone

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
    Detalle = models.CharField(max_length=50)
    Cantidad = models.IntegerField()
    PrecioVenta = models.DecimalField(max_digits=7, decimal_places=2)
    PrecioCosto = models.DecimalField(max_digits=7, decimal_places=2)

