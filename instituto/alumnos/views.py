
from django.shortcuts import render

from .models import Alumno,Genero

# Create your views here.


def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)


def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)


def base(request):
    context={}
    return render(request, 'alumnos/base.html', context)    


def home(request):
    context={}
    return render(request, 'alumnos/home.html', context)    