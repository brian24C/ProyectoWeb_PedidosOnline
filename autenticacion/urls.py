from django.urls import path
from .views import VRegistro, cerrar_sesion, logear



urlpatterns = [
  
    path("", VRegistro.as_view(), name="Autenticacion"),  # "as_view" para que nos muestre la "class" como una vista

    path("cerrar_sesion", cerrar_sesion, name="cerrar_sesion"), 

    path("logear", logear, name="logear"), 
]
  

 