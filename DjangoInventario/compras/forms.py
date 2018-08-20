from django.forms import ModelForm
from .models import Producto,Venta


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        exclude = ['id']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude = ['idVenta']
