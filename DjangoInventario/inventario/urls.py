from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    # Examples:
    # url(r'^$', 'inventario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-sb-admin/', include('django_sb_admin.urls')),
]

from compras import views as compras_views
# Use include() to add URLS from the compras application and authentication system
urlpatterns += [
    url(r'^', include('compras.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns += [
    url(r'^', RedirectView.as_view(url='/home/', permanent=True)),
]

urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]