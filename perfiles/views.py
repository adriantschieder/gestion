from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import MensajeriaInterna, Perfil_Usuario
from django.contrib.auth import update_session_auth_hash 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CambiarContrasenia

def profile(request, id):
    user= User.objects.get(id=id)
    perfil= Perfil_Usuario.objects.get(usuario_id = id)
    form = CambiarContrasenia(request.user, request.POST) 
    if form.is_valid(): 
        user = form.save() 
        update_session_auth_hash(request, user) 
        # Important! 
        messages.success(request, 'Su contraseña ha sido actualizada!') 
        return redirect('perfil') 
    else: 
        messages.error(request, 'Por favor, corrija el error.') 
    return render(request, 'profile.html', {"user":user,"perfil": perfil,"form": form})

def profileactualizado(request, id):
    form = CambiarContrasenia(request.user) 
    if request.method=="POST": 
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        telefono=request.POST['telefono']
        direccion=request.POST['direccion']
        ciudad=request.POST['ciudad']
        provincia=request.POST['provincia']
        user= User.objects.get(id=id)
        user.fist_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        perfil= Perfil_Usuario.objects.get(usuario_id = id)
        perfil.direccion = direccion
        perfil.ciudad = ciudad
        perfil.provincia = provincia
        perfil.telefono = telefono
        perfil.save()
        form = CambiarContrasenia(request.user, request.POST) 
        if form.is_valid(): 
            user = form.save() 
            update_session_auth_hash(request, user) 
            # Important! 
            messages.success(request, 'Su contraseña ha sido actualizada!') 
            return redirect('perfil') 
        else: 
            messages.error(request, 'Por favor, corrija el error.') 
    return render(request, 'profile.html', {"user":user,"perfil": perfil,"form": form})

def avataractualizado(request,id):
    if request.method=="POST" and request.FILES['subiravatar']:
        subiravatar=request.FILES['subiravatar']
        perfil= Perfil_Usuario.objects.get(usuario_id = id)
        perfil.avatar=subiravatar
        perfil.save()
        user= User.objects.get(id=id)
        return render(request, 'profile.html', {"user":user,"perfil": perfil})

def borrarusuario(request,id):
    usuario=User.objects.get(id=id)
    usuario.delete()
    return redirect('login')

def list_user(request):
    user= User.objects.all()
    perfil= Perfil_Usuario.objects.all()
    return render(request, 'list-user.html', {"user":user,"perfil": perfil})

def leermail(request,id):
    user= User.objects.all()
    mensajealeer=MensajeriaInterna.objects.get(id=id)
    return render(request, 'leer.html',{"mensajealeer": mensajealeer, "user": user})

def leerenviados(request,id):
    user= User.objects.all()
    mensajealeer=MensajeriaInterna.objects.get(id=id)
    return render(request, 'leerenviados.html',{"mensajealeer": mensajealeer, "user": user})

def bandeja(request):
    user=User.objects.all()
    bandejadeentrada = MensajeriaInterna.objects.filter(destinatario=request.user.id)
    return render(request, 'bandeja.html', {"bandejadeentrada":bandejadeentrada, "user": user})

def enviados(request):
    user=User.objects.all()
    enviado = MensajeriaInterna.objects.filter(remitente=request.user.id)
    return render(request, 'enviados.html', {"enviado":enviado, "user": user})

def redactarmail(request):
    if request.method == "POST":
        destinatario = User.objects.get(pk = request.POST["destinatario"])
        remitente = request.POST["remitente"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]
        mensajeria=MensajeriaInterna.objects.create(
            destinatario = destinatario,
            remitente = remitente,
            asunto = asunto,
            mensaje = mensaje,
        )
        return redirect('enviados')
    user= User.objects.all()
    return render(request, 'redactar.html',{"user":user})

def redactar(request,id):
    if request.method == "POST":
        destinatario = User.objects.get(pk = request.POST["destinatario"])
        remitente = request.POST["remitente"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]
        mensajeria=MensajeriaInterna.objects.create(
            destinatario = destinatario,
            remitente = remitente,
            asunto = asunto,
            mensaje = mensaje,
        )
        return redirect('enviados')
    user= User.objects.get(id=id)
    return render(request, 'redactar_usuario.html',{"user":user})

def borrar(request,id):
    mail=MensajeriaInterna.objects.get(id=id)
    mail.delete()
    return redirect('bandeja')

