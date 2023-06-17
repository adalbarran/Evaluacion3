#from django.conf.urls import url
from django.urls import path, include
from  . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

  path('', views.index, name='index'),
  
  path('informacion', views.informacion, name='informacion'),


  path("accounts/", include("django.contrib.auth.urls")),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
