from rest_cafeteria.viewsLogin import login
from django.urls import path

from rest_cafeteria.views import lista_alimentos,detalle_alimentos
from rest_cafeteria.viewsLogin import login

urlpatterns = [
    path('lista_alimentos',lista_alimentos,name='lista_alimentos'),
    path('detalle_alimentos/<id>',detalle_alimentos,name='detalle_alimentos'),
    path('login',login,name='login'),
]