from ssl import create_default_context
from tabnanny import verbose
from typing import OrderedDict
from zlib import DEF_BUF_SIZE
from django.db import models
#from django.contrib.auth.models import User   <-- MEDIANO IMPORTANTE :  Si pongo este codigo entonces la linea 15 ya no lo pondría.
from django.contrib.auth import get_user_model # esta "get_user_model" nos dará el usuario ACTIVO

from TiendaU.models import Producto

from django.db.models import F, Sum, FloatField

# Create your models here.

User=get_user_model()    #es para obtener el usuario que se ha logeado en ese momento, es decir el usuario ACTIVO

class Pedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)

    

    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*("cantidad"), output_field=FloatField)

        )["total"]

    def __str__(self):
        return self.id





    class Meta:
        db_table="pedidos"
        verbose_name="pedido"
        verbose_name_plural="pedidos"
        ordering=["id"]


class LineaPedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    creat_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"

    class Meta:
        db_table="lineapedidos"
        verbose_name="Linea Pedido"
        verbose_name_plural="Lineas Pedidos"
        ordering=["id"]
