
from django.forms import ModelForm
from django import forms
from .models import Automovil, Mecanico, Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios 
        #fields = ['ID', 'Nombre', 'Encargado', 'Tipo de Servicio', 'fecha_creacion'] 
   
        fields = '__all__' 
