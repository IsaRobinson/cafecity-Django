from django import forms
from django.forms import ModelForm
from .models import postulacionConcurso

class ConcursoForm(ModelForm):
    class Meta:
        model = postulacionConcurso
        fields = ['nombreAlimento','descripcionAlimento','precioAlimento']