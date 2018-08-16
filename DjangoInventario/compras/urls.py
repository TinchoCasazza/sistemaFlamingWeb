from django.conf.urls import include, url
from . import views

# URLs del Modulo Compras 

urlpatterns = [
         url(r'^/compra', views.compra),
         url(r'^$', views.index),
         url(r'^$/productos', views.productos),
]