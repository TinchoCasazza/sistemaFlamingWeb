from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Producto
from .models import Proveedor
# -*- coding: utf-8 -*-
# Create your views here.

def inicio(request):
        return render(request, 'inicio.html', {})

def productos(request):
        lista_productos = Producto.objects.all()
        return render(request, 'productos.html', {'lista_productos':lista_productos})

def proveedores(request):
        lista_proveedores = Proveedor.objects.all()
        return render(request, 'proveedores.html', {'lista_proveedores':lista_proveedores})

from .models import ProductoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def Alta_Producto(request):
    form = ProductoForm(request.POST) # Bound form
    return render(request, 'producto_form.html', {'form': form})