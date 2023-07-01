from django.contrib import admin
from .models import Automovil,Mecanico,Servicios

# Register your models here.
admin.site.register(Automovil)
admin.site.register(Mecanico)
admin.site.register(Servicios)