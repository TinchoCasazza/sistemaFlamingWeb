from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .models import Producto
# -*- coding: utf-8 -*-
# Create your views here.

def inicio(request):
        return render(request, 'inicio.html', {})

def productos(request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos':productos})

from .models import ProductoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def Alta_Producto(request):
    form = ProductoForm(request.POST) # Bound form
    return render(request, 'producto_form.html', {'form': form})