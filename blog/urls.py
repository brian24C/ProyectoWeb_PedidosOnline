from django.urls import path

from . import views          #el punto significa que me dirige  a la raiz de dónde estoy 


urlpatterns = [
    path("", views.blog, name="Blog"),
    path("categoria/<int:categoria_id>/", views.categoria, name="categoria"),  #"<categoria_id>/": los "<>" es para especificar que es un parametro       (7:45 video41)
]                                                                                                       #con parametros me refiero a que cuando pongas un valor (en este caso un 1 o 2) , por ejem: http://localhost:8000/blog/categoria/1                                        
                                                                                                        # y luego ese valor irá a la funcion "def categoria" de views.py   

