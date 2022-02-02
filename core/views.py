from django.shortcuts import redirect, render

from perfiles.models import Perfil_Usuario

def index(request):
    return render(request, 'index.html')