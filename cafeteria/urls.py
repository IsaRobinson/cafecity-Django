from django.urls import path
from .views import inicio
from .views import carta
from .views import nosotros
from .views import contacto
from .views import administrador,admin_del_alimento,admin_mod_alimento

urlpatterns = [
    path('',inicio,name="inicio"),
    path('carta',carta,name="carta"),
    path('nosotros',nosotros,name="nosotros"),
    path('contacto',contacto,name="contacto"),
    path('administrador',administrador,name="administrador"),
    path('administrador-borrar/<id>',admin_del_alimento,name='admin_del_alimento'),
    path('administrador-modificar/<id>',admin_mod_alimento,name='admin_mod_alimento')
]