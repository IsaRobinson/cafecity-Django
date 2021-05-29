from django.contrib import admin
from .models import Categoria, Alimento, TipoAlimento

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Alimento)
admin.site.register(TipoAlimento)
