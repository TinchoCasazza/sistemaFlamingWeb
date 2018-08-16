from django.shortcuts import render
from .models import Producto


# Create your views here.

def compra(request):
        return render(request, 'compras/compra.html', {})

def home(request):
        return render(request, 'compras/home.html', {})

def index(request):
        return render(request, 'compras/index.html', {})

def productos(request):
        productos = Producto.objects.all()
        return render(request, 'compras/productos.html', {'productos':productos})