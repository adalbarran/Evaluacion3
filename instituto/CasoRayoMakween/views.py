from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'CasoRayoMakween/index.html', context)

def servicios(request):
    context={}
    return render(request, 'CasoRayoMakween/servicios.html', context)

def contacto(request):
    context={}
    return render(request, 'CasoRayoMakween/contacto.html', context)            

def MantencionMotor(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionMotor.html', context)     


def MantencionRuedas(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionRuedas.html', context)              

def MantencionAceite(request):
    context={}
    return render(request, 'CasoRayoMakween/MantencionAceite.html', context)           
