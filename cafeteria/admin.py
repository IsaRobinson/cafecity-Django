from django.contrib import admin
from .models import Categoria, Alimento, TipoAlimento,postulacionConcurso

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Alimento)
admin.site.register(TipoAlimento)
admin.site.register(postulacionConcurso)