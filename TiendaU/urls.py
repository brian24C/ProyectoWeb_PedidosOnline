from django.urls import path

from TiendaU import views


urlpatterns = [

    path("", views.tienda, name="Tienda"), 
    path("categoria/<int:categoria_id>/", views.categoria, name="Categoria"),
    
]
  

