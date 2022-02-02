from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.db.models import Q
from clientes.forms import registro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# import pkgutil
# from urllib import request
from django.shortcuts import redirect, render
from clientes.models import Clientes, Maquinarias, Arreglo_Maquinarias
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime

from perfiles.models import Perfil_Usuario
#Funciones para Pestaña de Arreglos
@login_required
def arreglos(request):
    arreglos = Arreglo_Maquinarias.objects.all()
    maquinarias = Maquinarias.objects.all()
    return render(request, 'arreglos.html', {"arreglos": arreglos, "maquinarias": maquinarias})
@login_required
def arreglos_cliente(request,id):
    maquinarias = Maquinarias.objects.get(id=id)
    arreglos = Arreglo_Maquinarias.objects.filter(maquinaria=id)
    return render(request, 'arreglos-cliente.html', {"arreglos": arreglos, "maquinarias": maquinarias})
@login_required
def arreglos_agregados(request):
    maquinarias = Arreglo_Maquinarias.objects.get(pk = request.POST['maquinarias'])
    fecha_arreglo = request.POST['fecha_arreglo']
    arreglo1 = request.POST['arreglo']
    arreglo = Arreglo_Maquinarias.objects.create(
        maquinarias = maquinarias,
        fecha_arreglo = fecha_arreglo,
        arreglo = arreglo1,
    )
    return redirect('../arreglos')
@login_required
def agregar_arreglos_clientes(request,id):
    maquinaria = Maquinarias.objects.get(pk = request.POST['maquinaria'])
    fecha_arreglo = request.POST['fecha_arreglo']
    if fecha_arreglo =="":
        fecha_arreglo = datetime.now()
    else:
        fecha_arreglo = fecha_arreglo
    arreglo1 = request.POST['arreglo']
    arreglo = Arreglo_Maquinarias.objects.create(
        maquinaria = maquinaria,
        fecha_arreglo = fecha_arreglo,
        arreglo = arreglo1,
    )
    return redirect(f'/clientes/arreglos-cliente/{id}')
@login_required
def eliminar_arreglo(request,id, idmaquina):
    arreglo = Arreglo_Maquinarias.objects.get(id=id)
    arreglo.delete()
    return redirect(f'/clientes/arreglos-cliente/{idmaquina}')
@login_required
def editar_arreglos_cliente(request,id,idmaquina):
    maquinarias = Maquinarias.objects.get(id=idmaquina)
    arreglos = Arreglo_Maquinarias.objects.get(id=id)
    return render(request, 'ver-arreglos.html', {"arreglos": arreglos, "maquinarias": maquinarias})
@login_required
def arreglos_editados(request,id,idmaquina):
    maquinaria = Maquinarias.objects.get(pk = request.POST['maquinaria'])
    fecha_arreglo = request.POST['fecha_arreglo']
    arreglo1 = request.POST['arreglo']
    arreglo = Arreglo_Maquinarias.objects.get(id=id)
    arreglo.fecha_arreglo = fecha_arreglo
    arreglo.arreglo = arreglo1
    arreglo.save()
    return redirect(f'/clientes/arreglos-cliente/{idmaquina}')


#FIN Funciones para Pestaña de Arreglos

# funciones para pestaña de maquinarias
@login_required
def maquinarias(request):
    clientes = Clientes.objects.all()
    maquinarias = Maquinarias.objects.all()
    return render(request, 'maquinarias.html', {"maquinarias": maquinarias,"clientes": clientes})
@login_required
def agregar_maquinas(request):
    propietario = Clientes.objects.get(pk = request.POST["propietario"])
    tipo = request.POST['tipo']
    modelo = request.POST['modelo']
    marca = request.POST['marca']
    maquinarias = Maquinarias.objects.create(
        propietario = propietario,
        tipo = tipo,
        modelo = modelo,
        marca = marca,
    )
    return redirect('../maquinarias')
@login_required
def agregar_maquinas_clientes(request,id):
    propietario = Clientes.objects.get(pk = request.POST['propietario']) #el problema era que obtenia un string y no lo tomaba como una instancia
    tipo = request.POST['tipo']
    modelo = request.POST['modelo']
    marca = request.POST['marca']
    maquinarias = Maquinarias.objects.create(
        propietario = propietario,
        tipo = tipo,
        modelo = modelo,
        marca = marca,
    )
    return redirect(f'../maquinarias-cliente/{id}')
@login_required
def maquinarias_cliente(request,id):
    clientes = Clientes.objects.get(id=id)
    maquinarias = Maquinarias.objects.filter(propietario_id=id)
    return render(request, 'maquinarias-cliente.html', {"maquinarias": maquinarias,"clientes": clientes})
@login_required
def editar_maquinarias(request,id):
    maquinarias = Maquinarias.objects.get(id=id)
    return render (request, "editar_maquinarias.html", {"maquinarias": maquinarias})


@login_required
def maquinaria_editada(request,idmaquina,idpropietario):
    propietario1 = request.POST['propietario']
    tipo = request.POST['tipo']
    modelo = request.POST['modelo']
    marca = request.POST['marca']
    maquinarias = Maquinarias.objects.get(id=idmaquina)
    maquinarias.tipo = tipo
    maquinarias.modelo = modelo
    maquinarias.marca = marca
    maquinarias.save()
    return redirect(f'/clientes/maquinarias-cliente/{idpropietario}')
@login_required
def maquinaria_editada2(request,idmaquina):
    propietario = request.POST['propietario']
    tipo = request.POST['tipo']
    modelo = request.POST['modelo']
    marca = request.POST['marca']
    maquinarias = Maquinarias.objects.get(id=idmaquina)
    maquinarias.tipo = tipo
    maquinarias.modelo = modelo
    maquinarias.marca = marca
    maquinarias.save()
    return redirect(f'/clientes/maquinarias/')
@login_required
def editar_maquinarias_cliente(request,id):
    maquinarias = Maquinarias.objects.get(id=id)
    return render(request, 'editar_maquinarias_cliente.html', {"maquinarias": maquinarias})
@login_required
def eliminar_maquinaria(request,id,idpropietario):
    maquinarias = Maquinarias.objects.get(id=id)
    maquinarias.delete()
    return redirect(f'/clientes/maquinarias-cliente/{idpropietario}')

    
    #Funciones para Pestaña de Clientes
@login_required
def clientes(request):
    abuscar = request.GET.get("clientebuscado")
    cliente = Clientes.objects.all()

    if abuscar:
        cliente = Clientes.objects.filter(
            Q(empresa__icontains = abuscar) |
            Q(cuit__icontains = abuscar) |
            Q(domicilio__icontains = abuscar)
        ).distinct()

    return render(request, 'clientes.html', {"clientes":cliente})
@login_required
def create(request):
    empresa = request.POST['empresa']
    condicion_iva = request.POST['iva']
    domicilio = request.POST['domicilio']
    telefono = request.POST['telefono']
    mail = request.POST['mail']
    cuit = request.POST['cuit']
    clientes = Clientes.objects.create(
        empresa = empresa,
        condicion_iva = condicion_iva,
        cuit = cuit,
        domicilio = domicilio,
        telefono = telefono,
        mail = mail,
    )
    return redirect('../listado')
class Client_edit(LoginRequiredMixin,UpdateView):
    model = Clientes
    success_url = "/clientes/listado/"
    fields = ['id','empresa','domicilio','condicion_iva','cuit','telefono','mail']
    template_name="clientes_form.html"
class Client_delete(LoginRequiredMixin,DeleteView):
    model = Clientes
    success_url = "/clientes/listado/"
    template_name = "clientes_confirm_delete.html"
     
#FIN Funciones para Pestaña de Clientes
@login_required
def eliminar(request,id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('../listado')    
#FIN Funciones para Pestaña de Clientes
#LOGIN
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=password)
            if user is not None:
                login(request,user)
                avatar=Perfil_Usuario.objects.filter(usuario_id=request.user.id)
                return render(request, 'index-admin.html', {"mensaje": f'Bienvenido {usuario}',"avatar":avatar[0].avatar.url})
            else:
                return render(request, 'login.html', {"mensaje": f'Intentalo nuevamente'})
        else:
            return render(request, 'login.html', {"mensaje": f'Algunos de los datos son incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form':form})

#register
def register(request):
    if request.method=='POST':
        # form = UserCreationForm(request.POST)
        form = registro(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            return render(request, 'index-admin.html', {"mensaje": f'Bienvenido {usuario}'})
    else:
        # form = UserCreationForm()
        form = registro()
    return render(request, "register.html", {'form':form})