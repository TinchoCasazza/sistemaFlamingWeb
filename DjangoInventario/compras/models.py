from django.db import models
from django.utils import timezone

# Create your models here.


class Proveedor(models.Model):
    Id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Nombre =  models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Documento = models.CharField(max_length=12)
