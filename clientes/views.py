from pickle import GET
from django.db.models import Q
import pkgutil
from urllib import request
from django.shortcuts import redirect, render
from clientes.models import Clientes, Maquinarias, Arreglo_Maquinarias
#Funciones para Pestaña de Arreglos
def arreglos(request):
    arreglos = Arreglo_Maquinarias.objects.all()
    maquinarias = Maquinarias.objects.all()
    return render(request, 'arreglos.html', {"arreglos": arreglos, "maquinarias": maquinarias})

def arreglos_cliente(request,id):
    maquinarias = Maquinarias.objects.get(id=id)
    arreglos = Arreglo_Maquinarias.objects.filter(maquinaria=id)
    return render(request, 'arreglos-cliente.html', {"arreglos": arreglos, "maquinarias": maquinarias})

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

def agregar_arreglos_clientes(request,id):
    maquinaria = Maquinarias.objects.get(pk = request.POST['maquinaria'])
    fecha_arreglo = request.POST['fecha_arreglo']
    arreglo1 = request.POST['arreglo']
    arreglo = Arreglo_Maquinarias.objects.create(
        maquinaria = maquinaria,
        fecha_arreglo = fecha_arreglo,
        arreglo = arreglo1,
    )
    return redirect(f'/clientes/arreglos-cliente/{id}')

def eliminar_arreglo(request,id, idmaquina):
    arreglo = Arreglo_Maquinarias.objects.get(id=id)
    arreglo.delete()
    return redirect(f'/clientes/arreglos-cliente/{idmaquina}')

def editar_arreglos_cliente(request,id,idmaquina):
    maquinarias = Maquinarias.objects.get(id=idmaquina)
    arreglos = Arreglo_Maquinarias.objects.get(id=id)
    return render(request, 'ver-arreglos.html', {"arreglos": arreglos, "maquinarias": maquinarias})

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

def maquinarias(request):
    clientes = Clientes.objects.all()
    maquinarias = Maquinarias.objects.all()
    return render(request, 'maquinarias.html', {"maquinarias": maquinarias,"clientes": clientes})

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


    #Funciones para Pestaña de Clientes
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

def clientes_editar(request,id):
    clientes = Clientes.objects.get(id=id)
    return render(request, 'clientes-editar.html', {"clientes": clientes})

def clientes_editados(request,id):
    id = request.POST['id']
    empresa = request.POST['empresa']
    condicion_iva = request.POST['iva']
    cuit = request.POST['cuit']
    domicilio = request.POST['domicilio']
    telefono = request.POST['telefono']
    mail = request.POST['mail']
    clientes = Clientes.objects.get(id=id)
    clientes.empresa = empresa
    clientes.condicion_iva = condicion_iva
    clientes.cuit = cuit
    clientes.domicilio = domicilio
    clientes.telefono = telefono
    clientes.mail = mail
    clientes.save()
    return redirect('../listado')

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

def eliminar(request,id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('../listado')    
#FIN Funciones para Pestaña de Clientes