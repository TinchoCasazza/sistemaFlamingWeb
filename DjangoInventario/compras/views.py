from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Producto
from .models import ModelCompra
from .models import Proveedor
from . import forms
# -*- coding: utf-8 -*-
# Create your views here.

def inicio(request):
        return render(request, 'inicio.html', {})

def productos(request): 
        if request.method == 'POST':
                if request.POST['IndiceBorrar'] > 0: 
                        indice = request.POST['IndiceBorrar']
                        productos = Producto.objects.all().order_by('Nombre')
                        productos[int(indice)].delete()
                        lista_productos = Producto.objects.all().order_by('Nombre') 
                        formProductos = forms.ProductoForm() 
                        return render(request, 'productos.html', {'lista_productos':lista_productos , 'form' : formProductos})
                else:
                        formProductos = forms.ProductoForm(request.POST)
                        if formProductos.is_valid():
                                obj = Producto()
                                obj = formProductos.save(commit=False)
                                obj.save()       
                                lista_productos = Producto.objects.all().order_by('Nombre')               
        else:
                lista_productos = Producto.objects.all().order_by('Nombre')
                formProductos = forms.ProductoForm()
        return render(request, 'productos.html', {'lista_productos':lista_productos , 'form' : formProductos})

def viewcompras(request): 
        
        lista_compras = ModelCompra.objects.all() 
        formCompras = forms.CompraForm()
        return render(request, 'compras_flaming.html', {'lista_compras':lista_compras})

def proveedores(request):        
        if request.method == 'POST':
                formProveedores = forms.ProveedorForm(request.POST)
                if formProveedores.is_valid():
                        obj = Proveedor()
                        obj = formProveedores.save(commit=False)
                        obj.save()
                        lista_proveedores = Proveedor.objects.all().order_by('Nombre')
        else:
                lista_proveedores = Proveedor.objects.all().order_by('Nombre')
                formProveedores = forms.ProveedorForm()
        return render(request, 'proveedores.html', {'form':formProveedores, 'lista_proveedores':lista_proveedores})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

def Alta_Producto(request):
    formProductos = form.ProductoForm() # Bound form
    return render(request, 'producto_form.html', {'form': formProductos})


from django.contrib.auth import authenticate, login

CRITICAL = 50
def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        return render(request, 'inicio.html', {})
                else:
                        messages.set_level(request, messages.WARNING)
                        messages.add_message(request, CRITICAL, 'Datos Incorrectos.')
                        return render(request, 'login.html' ,{'error': messages} )

        else: 
                return render(request, 'login.html' ,{} )



