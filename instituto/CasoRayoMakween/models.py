from typing import Any, Dict, Tuple
from django.db import models


# Create your models here.


class Automovil(models.Model):

    patente            = models.CharField(primary_key=True, max_length=10)
    marca    = models.CharField(max_length=25, blank=False, null=False)
    color    = models.CharField(max_length=10, blank=False, null=False)

    desc_automovil  = models.TextField(max_length=500)

    imagen_automovil = models.ImageField(null=True,blank=True)


    def __str__(self):
        return str(self.Automovil)


class Mecanico(models.Model):
    rut = models.AutoField(db_column="rut", primary_key=True)
    id_servicio = models.ForeignKey('Servicios', on_delete=models.CASCADE, db_column='id')

    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)  
  
    def __str__(self):
        return self.nombre  # Puedes devolver el nombre, el rut u otro campo representativo






class Servicios(models.Model):

    ID_servicio = models.AutoField(primary_key=True, db_column='id')

    Encargado = models.CharField(max_length=50, verbose_name='Encargado')
    Tipo_de_Servicio = models.CharField(max_length=90, blank=True, null=True, verbose_name='Tipo_de_Servicio')
    fecha_creacion = models.DateField(auto_now=False, verbose_name='fecha_creacion')



    def __str__(self):
        return str(self.Encargado)

    class Meta:
        ordering = ['Encargado']

def delete(self, using=None, keep_parents=False):
    if self.img:
        self.img.storage.delete(self.img.name)
    return super().delete(using=using, keep_parents=keep_parents)

