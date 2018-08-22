from django.forms import ModelForm
from .models import Producto,Venta,Proveedor


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        exclude = ['id']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude = ['idVenta']
