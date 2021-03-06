from django.conf.urls import include, url
from django.contrib import admin
from .views import hola, fecha_actual, horas_adelante

urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hola/$', hola),
    url(r'fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante)
]
