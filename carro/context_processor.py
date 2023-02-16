   
   
# en este codigo solo entrará en el if si está autenticado
# y luego funcionará el "for" solo si agregé a "session" la clave "carro" . (4:38 video66)

def importe_total_carro(request):

      total = 0

      if request.user.is_authenticated:
            for key, value in request.session["carro"].items():   
                  total = total + float(value["precio"])

      else:
            total="debes iniciar session"""

      return {"importe_total_carro": total} 



      #Super importante 11

      #hacer login y session es diferente. Al añadir un producto agrego a "session" un diccionario {  "carro":{ id:{id,nombre,precio},id:{id,nombre,precio} }  }
                                                                                                             #[Este espacio ↑ es de "def agregar" de carro.py]
      # cuando yo hago login o me creo una cuenta, quiere decir que ya me autentiqué (ver linea 25 y 54 de /autenticacion/views.py)






"""

-------Si entro a la web por primera vez entonces me dará error porque en el bucle "for" yo no tengo en "session" la clave "carro" (porque yo todavía no entré en la clase "Carro" de carro.py)------------

def importe_total_carro(request):

      total = 0


      for key, value in request.session["carro"].items():        #he podido comprobar más o menos esto:
                                                                 # si yo pongo "if request.session is true" y si esque es true q me arroje el total
                                                                 # lo que sucede es que SÍ me arroja el total. quiere decir quizás que el "request.session" ya se tiene desde un inicio (es decir la primera vez que se inicia la app)
                                                                 # pero no cuando cuando le pones "request.session["carro"]" porque "carro" aun no está especificado cuando iniciar por primera vez la app   
                                                                 #una HIPÓTESIS es que se hace sesion cuando yo entro en la página, es decir el simple echo de entrar a mi app (la pagina web) ya es una sesion.

              total = total + float(value["precio"])

      return {"importe_total_carro": total}   """