from django.template.context_processors import request
from perfiles.models import Perfil_Usuario
from django.contrib.auth import login

def avatar(request):
    if request.user.is_authenticated:
        avatar=Perfil_Usuario.objects.filter(usuario_id=request.user.id)
        return {"avatar1":avatar[0].avatar.url}
    else:
        avatar=Perfil_Usuario.objects.all()
        return {"avatar": avatar}
