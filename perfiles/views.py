from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import MensajeriaInterna, Perfil_Usuario

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
