from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Producto
from .models import Proveedor
from . import forms
# -*- coding: utf-8 -*-
# Create your views here.

def inicio(request):
        return render(request, 'inicio.html', {})

def productos(request): 
        if request.method == 'POST':
                formProductos = forms.ProductoForm(request.POST)
                if formProductos.is_valid():
                        obj = Producto()
                        obj = formProductos.save(commit=False)
                        obj.save()       
                        lista_productos = Producto.objects.all()               
        else:
                lista_productos = Producto.objects.all()
                formProductos = forms.ProductoForm()
        return render(request, 'productos.html', {'lista_productos':lista_productos , 'form' : formProductos})

def proveedores(request):
        lista_proveedores = Proveedor.objects.all()
        return render(request, 'proveedores.html', {'lista_proveedores':lista_proveedores})

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def Alta_Producto(request):
    formProductos = form.ProductoForm() # Bound form
    return render(request, 'producto_form.html', {'form': formProductos})


