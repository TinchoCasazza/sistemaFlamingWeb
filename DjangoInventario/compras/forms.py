from django.forms import ModelForm
from .models import Producto 
from .models import Proveedor 

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        exclude = ['id']

