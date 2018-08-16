from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'inventario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('compras.urls')),
    url(r'^django-sb-admin/', include('django_sb_admin.urls')),
    url(r'^home/', 'compras.views.home', name='home'),
    url(r'^productos_list/', 'compras.views.productos', name='productos'),


]
