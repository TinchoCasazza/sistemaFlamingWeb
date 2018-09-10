from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout, login_required 
from django.conf import settings

# URLs del Modulo Compras 
APPEND_SLASH = False
urlpatterns = [

    #Login 
    url(r'^$', views.login, name = 'login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'inicio/$', login_required(views.inicio), name = 'inicio_url'),

    #Productos 
    url(r'productos/$', login_required(views.productos), name = 'productos_url'),
    url(r'productos/eliminar_producto/$', login_required(views.productos_eliminar), name = 'productos_eliminar_url'),
    url(r'productos/editar_producto/$', login_required(views.productos_editar), name = 'productos_editar_url'),
    
    #Proveedores
    url(r'proveedores/$', login_required(views.proveedores), name = 'proveedores_url'),
    url(r'proveedores/eliminar_proveedor/$', login_required(views.proveedores_eliminar), name = 'proveedores_eliminar_url'),
    url(r'proveedores/editar_proveedor/$', login_required(views.proveedores_editar), name = 'proveedores_editar_url'),

    #Compras
    url(r'compras/$', login_required(views.viewcompras), name = 'compras_url'),
]