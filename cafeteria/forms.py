from django import forms
from django.forms import ModelForm
from .models import postulacionConcurso,Alimento

class ConcursoForm(ModelForm):
    class Meta:
        model = postulacionConcurso
        fields = ['nombreAlimento','descripcionAlimento','precioAlimento']

class AlimentoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = ['idAlimento','nombre','descripcion','precio']
        