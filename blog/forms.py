from django import forms
from .models import Comentario, Post

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
