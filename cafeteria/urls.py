from django.urls import path
from .views import inicio
from .views import carta
from .views import nosotros
from .views import contacto

urlpatterns = [
    path('',inicio,name="inicio"),
    path('/carta',carta,name="carta"),
    path('/nosotros',nosotros,name="nosotros"),
    path('/contacto',contacto,name="contacto")
]