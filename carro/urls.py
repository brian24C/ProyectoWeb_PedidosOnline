from django.urls import path

from carro import views

                    #DATITO
app_name="carro"  # es para que no haya colision entre "name" (16:00 video 56 )

urlpatterns = [

    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"), 
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/<int:producto_id>/", views.limpiar_carro, name="limpiar"),
    
]
  

