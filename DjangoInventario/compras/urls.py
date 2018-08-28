from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login, logout, login_required 
from django.conf import settings

# URLs del Modulo Compras 
APPEND_SLASH = False
urlpatterns = [
    url(r'^$', views.login, name = 'login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'inicio/$', login_required(views.inicio), name = 'inicio_url'),
    url(r'productos/$', login_required(views.productos), name = 'productos_url'),
    url(r'producto_form/$', login_required(views.Alta_Producto), name = 'ProductoAlta_url'),
    url(r'proveedores/$', login_required(views.proveedores), name = 'proveedores_url'),
    url(r'compras/$', login_required(views.viewcompras), name = 'compras_url'),
]