
from turtle import st


class Carro:

    def __init__(self, request):

        self.request=request
        self.session=request.session   # Es una como una variable super global es decir, una vez se agregue productos al carro se guardará en self.carro, luego podré utilizar self.session.get("carro") "globalmente" (a través de todas las páginas de mi sitio web)
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}  #esta doble "=" hace que en el diccionario se "sesion" se cree la clave "carro" con su valor "{}"
        
        
        self.carro=carro

    def agregar(self, producto):

            if (str(producto.id) not in self.carro.keys()):   #el Keys los pone en lista por ejm ---> [‘a’,’b’,’c’,’d’]

                self.carro[producto.id]={

                    "producto_id":producto.id,
                    "nombre":producto.nombre,
                    "precio":str(producto.precio),
                    "cantidad":1,
                    "imagen":producto.imagen.url

                }
            
            else:
                for key, value in self.carro.items():           #los items los pone en lista --> [(‘a’,1),(‘b’,2),(‘c’,3),(‘d’,4)]
                    if key==str(producto.id):
                        value["cantidad"]=value["cantidad"]+1
                        value["precio"]=float(value["precio"])+producto.precio
                        break
   
            self.guardar_carro()
        
    def guardar_carro(self):
            self.session["carro"]=self.carro
            self.session.modified=True

    def eliminar (self, producto):
            producto.id=str(producto.id)
            if producto.id in self.carro:
                del self.carro[producto.id]
                self.guardar_carro()
        
    def restar_producto(self, producto):
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1

                    value["precio"]=float(value["precio"])-producto.precio
                    
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    
                    break
            self.guardar_carro()

    def limpiar_carro(self):
            self.session["carro"]={}
            self.session.modified=True


        


        
