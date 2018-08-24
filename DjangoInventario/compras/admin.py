from django.contrib import admin
from .models import Proveedor
from .models import Producto
from .models import ModelCompra

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(ModelCompra)
