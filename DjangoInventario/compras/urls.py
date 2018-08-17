from django.conf.urls import include, url
from . import views

# URLs del Modulo Compras 

urlpatterns = [
        url(r'^home', views.home),
        url(r'^$/productos', views.productos),
]