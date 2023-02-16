from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

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

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)                    # el "upload_to es para tener que la imagen se guarde en /media/servicios"
    
    autor=models.ForeignKey(User, on_delete=models.CASCADE)     #relación 1 a varios (la clave foreana será el usuario el cual si este se va de nuestra página, entonces se eliminá todos los post que el hizo)
    categorias=models.ManyToManyField(Categoria)                #relación de varios a varios (una "categoria"(sotware, harware) puede estar en varios "Post" y este en varias "categorias")
    
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 
     
    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"

    def __str__(self):
        return self.titulo
