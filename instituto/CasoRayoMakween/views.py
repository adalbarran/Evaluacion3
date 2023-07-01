from django.shortcuts import render, redirect
from .models import Automovil,Mecanico,Servicios
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ServiciosForm
# Create your views here.
def index(request):
    context={}
    return render(request, 'CasoRayoMakween/index.html', context)



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




def servicios(request):
    servicios = Servicios.objects.all()
    context={"servicios":servicios}
    return render(request, 'CasoRayoMakween/servicios.html', context)



def gestionser(request):
    servicios = Servicios.objects.all()
    context={"servicios":servicios}
    return render(request, 'CasoRayoMakween/Edicion/gestionser.html', context)

def nuevoser(request):
    formulario = ServiciosForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestionser')
    return render(request, "CasoRayoMakween/Edicion/nuevoservicio.html", {"formulario": formulario})

def editarservicio(request, ID_servicio):
    servicio = Servicios.objects.get(ID_servicio=ID_servicio)
    formulario = ServiciosForm(request.POST or None, request.FILES or None, instance=servicio)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('gestionser')
    return render(request, "CasoRayoMakween/Edicion/editarservicio.html", {"formulario": formulario})

def borrarservicio(request, ID_servicio):
    servicios = Servicios.objects.get(ID_servicio = ID_servicio)
    servicios.delete()
    messages.success(request, '¡Servicio Eliminado!')
    return redirect('gestionser')







#GESTION USUARIOS
def login(request):
    return render(request, "Registration/login.html")

def salir(request):
    logout(request)
    return redirect('/')
