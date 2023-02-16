from django.shortcuts import render
from TiendaU.models import Producto, Categoria
# Create your views here.


def tienda (request):

    Tienda=Producto.objects.all()

    return render(request, "TiendaT/tienda.html", {"Tiendas":Tienda})

 

def categoria(request, categoria_id):               

    categoria=Categoria.objects.get(id=categoria_id)
    
    Tienda=Producto.objects.filter(categorias=categoria_id)  #si pongo esto "categorias=categoria_id" igual funcionaría
                                                                   #        categorias_id=categoria        <- con esto igual funciona
                                                                   #        categorias_id=categoria_id     <-tambien funciona
    return render(request, "TiendaT/categorias.html", {"categoria":categoria,"Tiendas":Tienda})