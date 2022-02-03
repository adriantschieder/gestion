from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Perfil_Usuario

def profile(request, id):
    if request.method=="POST":
        avataractualizado=Perfil_Usuario(request.POST, request.FILES)

    user= User.objects.get(id=id)
    perfil= Perfil_Usuario.objects.get(usuario_id = id)
    return render(request, 'profile.html', {"user":user,"perfil": perfil})

def list_user(request):
    user= User.objects.all()
    perfil= Perfil_Usuario.objects.all()
    return render(request, 'list-user.html', {"user":user,"perfil": perfil})
