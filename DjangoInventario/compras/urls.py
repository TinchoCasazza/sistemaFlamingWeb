from django.conf.urls import include, url
from . import views

# URLs del Modulo Compras 

urlpatterns = [
    url(r'^$', views.inicio, name = 'inicio_url'),
    url(r'productos/$', views.productos, name = 'productos_url'),
    url(r'producto_form/$', views.Alta_Producto, name = 'ProductoAlta_url'),
    url(r'proveedores/$', views.proveedores, name = 'proveedores_url'),
]