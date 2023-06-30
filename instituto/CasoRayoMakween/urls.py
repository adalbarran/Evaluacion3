#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

  path('', views.index, name='index'),
  
  path('servicios', views.servicios, name='servicios'),

  path('contacto', views.contacto, name='contacto'),

  path('MantencionMotor', views.MantencionMotor, name='MantencionMotor'),

  path('MantencionRuedas', views.MantencionRuedas, name='MantencionRuedas'),

  path('MantencionAceite', views.MantencionAceite, name='MantencionAceite'),

  path("accounts/", include("django.contrib.auth.urls")),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
