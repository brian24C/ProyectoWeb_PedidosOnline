from django.urls import path

from servicios import views

urlpatterns = [
    path("", views.servicios, name="Servicios"),  # el "name", me sirve para utilizarlo como referencia ejemplo en "base.html linea41"
]
  