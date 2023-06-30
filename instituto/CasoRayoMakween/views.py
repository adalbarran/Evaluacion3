from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'CasoRayoMakween/index.html')

def servicios(request):
    context={}
    return render(request, 'CasoRayoMakween/servicios.html')

def contacto(request):
    context={}
    return render(request, 'CasoRayoMakween/contacto.html')            

def MantencionMotor(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionMotor.html')     


def MantencionRuedas(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionRuedas.html')              

def MantencionAceite(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionAceite.html')           