from tkinter import Widget
from django import forms
from .models import Comentario, Post, Contacto

class Postform(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("titulo","subtitulo","portada_post", "cuerpo")

        widgets = {
            "titulo": forms.TextInput(attrs= {"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs= {"class": "form-control"}),
            #"autor": forms.Select(attrs= {"class": "form-control"}),
            "portada_post" : forms.FileInput (attrs= {"class": "form-control"}) ,
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"}),



        }


class Postedit(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("titulo", "cuerpo")

        widgets = {
            "titulo": forms.TextInput(attrs= {"class": "form-control"}),
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"})
        }


class Crear_comentario(forms.ModelForm):
    class Meta():
        model = Comentario
        fields = ( "cuerpo",)

        widgets = {
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"}),
        }


class Contacto(forms.ModelForm):

    class Meta():
        model = Contacto
        fields = ("nombre", "numero_telefono", "email", "cuerpo")

        Widgets = {
            "nombre": forms.TextInput(attrs= {"class": "form-control"}),
            "numero_telefono": forms.NumberInput(attrs= {"class": "form-control"}),
            "email": forms.EmailInput(attrs= {"class": "form-control"}),
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"}),

        }
