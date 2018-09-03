from django.forms import ModelForm
from .models import Producto,ModelCompra,Proveedor


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
    

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        exclude = ['id']

class CompraForm(ModelForm):
    class Meta:
        model = ModelCompra
        exclude = ['idCompra']
