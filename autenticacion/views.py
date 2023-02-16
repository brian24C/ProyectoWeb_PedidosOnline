from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages  # para que me salgan los mensajes de error cuando coloco algun dato erroneo en el formulario
# Create your views here.

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})


    def post(self, request):
        form=UserCreationForm(request.POST)  # recordar que el "POST" arroja un diccionario {clave:valor}
                                             # recordar que el "UserCreationForm" es como un form que se crea usualmente el los forms.py
                                             # y al igual que cuando en el "panel de adm" se guarda (save) un articulo y aparece en la base de datos, lo mismo sucede cuando utilizo el "metodo save" en la linea 23 
        if form.is_valid():

            usuario=form.save()    # el "save" hace q se guarden los usuarios registrados en mi app

            login(request, usuario)  # con esto hago que  despues de registrarse se queda en login 

            return redirect("Home") 

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})


        
def cerrar_sesion(request):

    logout(request) # elimina la sesion y el login. (leer comentarios de carro/context_processor.py)

    return redirect("Home")

def logear(request):

    if request.method == "POST":
        form=AuthenticationForm( data=request.POST)

        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")  #"usurname" se llama por defecto el cuadro (el campo username) del formulario
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')

            else:
                messages.error(request,"usuario no valido")

        else:
            messages.error(request,"informacion incorrecta")
    
    else:  
        form=AuthenticationForm()

    return render(request,"login/login.html",{"form":form})









