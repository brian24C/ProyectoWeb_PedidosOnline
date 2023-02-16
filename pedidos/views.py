from email import message
from urllib.robotparser import RequestRate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here. 

@login_required(login_url="/autenticacion/logear")  # es para redireccionar al "usuario" en el caso de que no esté logeado.
def procesar_pedido(request):                       
    pedido=Pedido.objects.create(user=request.user) #DATITO: parece que hay una diferencia cuando se usa "create" y "filter" (VER Linea 18 de TiendaU/views.py)
    carro=Carro(request)                                    #Ya que no puedo usar user_id=request.user
    lineas_pedido=list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,           #el "request.user" me da el id de la tabla usuarios "auth_user" DEL quien está logeado en ese instante.
            pedido=pedido,               #el "pedido" me da el id de la tabla "pedidos"

        ))

    LineaPedido.objects.bulk_create(lineas_pedido)   #"bulk_create" lo que haces es llevar el lote de "Lineas_pedido" a la BB.DD ( lote porque en la lista tenemos varios PRODUCTOS)
                                                     # si no entendiste --> (ver video 56 del curso de python pildoras informaticas)   
    enviar_mail(
        pedido=pedido,                               #se llama al pedido de la linea 17 (como es un objeto entonces podré utilizar sus atributos, llamar al id, user_id (VER linea 12 de pedidos.html)
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    )
    
    messages.success(request, "El pedido se ha creado correctamente") 

    return redirect("../tienda")

def enviar_mail(**kwargs):

    asunto="Gracias por el pedido"
    mensaje=render_to_string("email/pedidos.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
        "email": kwargs.get("emailusuario"),
        })

    mensaje_texto=strip_tags(mensaje)   #el strip_tags omite las etiquetas de la variable mensaje (aún no tengo claro este concepto, porque cuando yo quito el "strip_tags" funciona igual)
    from_email="brianjosuecastro@hotmail.com"
    #to="bry4n_jos43@hotmail.com"
    to=kwargs.get("emailusuario")              #esta línea va siempre y cuando el usuario tenga un correo registrado, sino me dará error y en ese caso tendría que poner la línea 56
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)  #el "html_message" es para espicificar que se envía un mensaje HTML
            



    

