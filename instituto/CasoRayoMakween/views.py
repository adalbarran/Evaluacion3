from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'CasoRayoMakween/index.html')

def servicios(request):
    context={}
<<<<<<< HEAD
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
=======
    return render(request, 'CasoRayoMakween/servicios.html')    
>>>>>>> 07a90271d453d4984d3ddc6c41f7f3d8c8d41c57
