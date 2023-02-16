from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.


def servicios (request):
 
    servicios=Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios":servicios})

    #Super importante objetos:  la variable servicios me dará: [objeto1, objeto2] 
    # cada objeto es una "clase" que contiene el "modelo" de "Servicio",
    #por eso yo puedo hacer llamadas como en la linea 19 de servicios.html
      
    #en cambio los "request.POST" o "request.GET" me dará 1 diccionario: {clave:valor}
    #por ejem: cuando se llena un formulario y al hacer click en un botón "enviar" y se manda la información por POST,
    #entonces la informacion se enviará en un diccionario que estará dentro de la petición(request), que a la ves 
    #que a la ves esta peticion se enviará a un servidor que leerá todo y  podrás ver la página.