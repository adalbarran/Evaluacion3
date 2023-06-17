#from django.conf.urls import url
from django.urls import path
from  . import views


urlpatterns = [

  path('index', views.index, name='index'),
  path('listadoSQL', views.listadoSQL, name='listadoSQL'),
  
  path('base', views.base, name='base'),
  path('', views.home, name='home'),

] 

