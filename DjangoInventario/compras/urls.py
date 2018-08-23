from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login 

# URLs del Modulo Compras 

urlpatterns = [
    url(r'^$', login, {'template_name':'login.html'}, name = 'login'),
    url(r'inicio/$', views.inicio, name = 'inicio_url'),
    url(r'productos/$', views.productos, name = 'productos_url'),
    url(r'producto_form/$', views.Alta_Producto, name = 'ProductoAlta_url'),
    url(r'proveedores/$', views.proveedores, name = 'proveedores_url'),
    url(r'compras/$', views.compras, name = 'compras_url'),

]