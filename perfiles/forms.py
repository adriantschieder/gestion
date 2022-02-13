from attrs import fields
from django.contrib.auth.forms import PasswordChangeForm
from django import forms


class CambiarContrasenia(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Actual",widget=forms.PasswordInput,help_text="Campo Requerido")
    new_password1 = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput,help_text="Campo Requerido")
    new_password2 = forms.CharField(label="Repite la Nueva Contraseña",widget=forms.PasswordInput,help_text="Campo Requerido")

    field_order = ['old_password', 'new_password1', 'new_password2']

