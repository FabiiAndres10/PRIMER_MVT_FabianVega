
from django.contrib import admin
from django.urls import path

from Familia.views import saludo, template_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name= 'saludo'),
    path('template_familia/', template_familia, name= 'template_familia')
]
