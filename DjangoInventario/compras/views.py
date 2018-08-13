from django.shortcuts import render

# Create your views here.

def compra(request):
        return render(request, 'compras/compra.html', {})

def home(request):
        return render(request, 'compras/home.html', {})
