from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'CasoRayoMakween/index.html')

def servicios(request):
    context={}
    return render(request, 'CasoRayoMakween/servicios.html')    