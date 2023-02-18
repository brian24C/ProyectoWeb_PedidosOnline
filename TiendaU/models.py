
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 
     
    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"

    def __str__(self):
        return self.nombre

class Producto(models.Model):    
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="Tienda", null=True, blank=True)                    # el "upload_to es para tener que la imagen se guarde en /media/servicios"
    precio=models.FloatField() 
    disponibilidad=models.BooleanField(default=True)

        
    categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)                  #relación 1 a varios

    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 
     
    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"


