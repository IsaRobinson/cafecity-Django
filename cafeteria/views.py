from django.shortcuts import render
from .models import Alimento
from .forms import ConcursoForm

# Create your views here.

def inicio(request):
    return render(request,'cafeteria/index.html')

def carta(request):
    listaAlimentos=Alimento.objects.all()
    datos={
        'alimentos':listaAlimentos
    }
    return render(request,'cafeteria/carta.html',datos) 

def nosotros(request):
    return render(request,'cafeteria/nosotros.html')

def contacto(request):
    datos={
        'form':ConcursoForm()
    }
    if(request.method=='POST'):
        formulario = ConcursoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardado correctamente'
    return render(request,'cafeteria/contacto.html',datos)