from django.shortcuts import render
from .models import Producto


# Create your views here.

def home(request):
        return render(request, 'home.html', {})


def productos(request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos':productos})
