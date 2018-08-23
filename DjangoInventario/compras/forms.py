from django.forms import ModelForm
from .models import Producto,Compra,Proveedor


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        exclude = ['id']

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        exclude = ['idCompra']
