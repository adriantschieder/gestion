from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Perfil_Usuario

def profile(request, id):
    user= User.objects.get(id=id)
    perfil= Perfil_Usuario.objects.get(usuario_id = id)
    return render(request, 'profile.html', {"user":user,"perfil": perfil})