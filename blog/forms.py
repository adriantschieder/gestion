from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("titulo", "autor", "cuerpo")

        widgets = {
            "titulo": forms.TextInput(attrs= {"class": "form-control"}),
            "autor": forms.Select(attrs= {"class": "form-control"}),
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"})



        }


class Postedit(forms.ModelForm):
    class Meta():
        model = Post
        fields = ("titulo", "cuerpo")

        widgets = {
            "titulo": forms.TextInput(attrs= {"class": "form-control"}),
            "cuerpo": forms.Textarea(attrs= {"class": "form-control"})



        }