from django.shortcuts import render
from .carro import Carro
from TiendaU.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)       #  -->                      <Producto: Teclado inalámbrico>      
                                                      #Producto.objects.all() --> [<Producto: Teclado inalámbrico>, <Producto: Teclado con cable>, <Producto: teclado simple>, <Producto: Raton gamer>, <Producto: Raton inalámbrico>]
                                                                               #    [<Producto: Producto object (1)>, <Producto: Producto object (2)>, <Producto: Producto object (3)>, <Producto: Producto object (4)>, <Producto: Producto object (5)>]
    carro.agregar(producto)
    return redirect("Tienda")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)      
                                                      
    carro.eliminar(producto)

    return redirect("Tienda")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)      
                                                      
    carro.restar_producto(producto)

    return redirect("Tienda")


def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")





