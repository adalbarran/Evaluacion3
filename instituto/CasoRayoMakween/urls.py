from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib import admin


urlpatterns = [

  path('', views.index, name='index'),
  
  path('servicios', views.servicios, name='servicios'),

  path('contacto', views.contacto, name='contacto'),

  path('MantencionMotor', views.MantencionMotor, name='MantencionMotor'),

  path('MantencionRuedas', views.MantencionRuedas, name='MantencionRuedas'),

  path('MantencionAceite', views.MantencionAceite, name='MantencionAceite'),



  path("accounts/", include("django.contrib.auth.urls")),

  #CRUD
  path('gestionser', views.gestionser, name='gestionser'),
  path('nuevoser', views.nuevoser, name='nuevoser'),  
  path('editarservicio/<ID_servicio>', views.editarservicio, name='editarservicio'),
  path('borrarservicio/<ID_servicio>', views.borrarservicio, name='borrarservicio'),

path('logout', views.signout, name='logout'),
path('login/', views.signin, name='login'),



] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
