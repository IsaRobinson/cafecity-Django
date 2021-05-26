from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'cafeteria/index.html')

def carta(request):
    return render(request,'cafeteria/carta.html') 

def nosotros(request):
    return render(request,'cafeteria/nosotros.html')

def contacto(request):
    return render(request,'cafeteria/contacto.html')