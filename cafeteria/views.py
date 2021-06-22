from django.shortcuts import render,redirect
from django.utils import tree
from .models import Alimento
from .forms import ConcursoForm, AlimentoForm

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

def administrador(request):
    listaAlimentos=Alimento.objects.all()
    datos={
        'alimentos':listaAlimentos
    }
    return render(request,'cafeteria/administrador.html',datos)

def admin_del_alimento(request,id):
    alimento = Alimento.objects.get(idAlimento=id)
    alimento.delete()

    return redirect(to='administrador')

def admin_mod_alimento(request,id):
    alimento = Alimento.objects.get(idAlimento=id)

    datos={
        'form':AlimentoForm(instance=alimento)
    }  
    if(request.method=='POST'):
        formulario = AlimentoForm(data=request.POST, instance=alimento)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Guardado correctamente'

    return render(request,'cafeteria/adminmodalimento.html',datos)