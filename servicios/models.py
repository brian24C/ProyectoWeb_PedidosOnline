
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="servicios")   # el "upload_to es para tener que la imagen se guarde en /media/servicios"
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 
     
    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"

    def __str__(self):
        return self.titulo       #esto para que en el panel dentro de "servicios" me aparezca el titulo de cada servicio