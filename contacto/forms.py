from django import forms


class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="nombre", required=True)
    email=forms.EmailField(label="email", required=True)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)