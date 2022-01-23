from django.urls import path
from .views import (
     #funciones de Clientes
     Client_delete, Client_edit, clientes,create, 
     #funciones de Maquinarias
     maquinarias,agregar_maquinas,editar_maquinarias,maquinaria_editada2,maquinarias_cliente,eliminar_maquinaria,maquinaria_editada,
     editar_maquinarias_cliente,agregar_maquinas_clientes,

     #funciones de Arreglos
     arreglos,arreglos_cliente,agregar_arreglos_clientes,arreglos_editados,eliminar_arreglo,
     #login
     login_request, register,
     )
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('arreglos/',arreglos, name ='arreglos'),
     path('arreglos-cliente/<id>', arreglos_cliente, name = 'arreglosclientes'),
     path('arreglos-agregados/<int:id>',agregar_arreglos_clientes, name='arreglos-agregados'),
     path('arreglos-editados/<id>/<idmaquina>', arreglos_editados, name='arregloseditados'),
     path('eliminar-arreglo/<id>/<idmaquina>', eliminar_arreglo, name = 'eliminar-arreglo'),
     #------------------------------------------------------------
     path('maquinarias/', maquinarias, name='maquinarias'),
     path('agregar_maquinarias/', agregar_maquinas),
     path('agregar_maquinarias_cliente/<id>', agregar_maquinas_clientes),
     path('maquinarias-cliente/<id>', maquinarias_cliente),
     path('eliminar_maquinaria/<id>/<idpropietario>/',eliminar_maquinaria),
     path('editar_maquinarias_cliente/<id>/',editar_maquinarias_cliente),
     path('editar_maquinarias/<id>/',editar_maquinarias),
     path('editar_maquinarias/maquinaria_editada2/<idmaquina>', maquinaria_editada2),
     path ("edit_maquinarias_cliente", editar_maquinarias_cliente),
     path('editar_maquinarias_cliente/maquinaria_editada/<idmaquina>/<idpropietario>', maquinaria_editada),
     path ("maquinarias/", maquinarias, name = "maquinarias"),
     path ("agregar_maquinarias/", agregar_maquinas),
     #------------------------------------------------------------
     path('listado/', clientes, name='clientes'),
     path('add/', create),
     path('client-edit/<pk>/', Client_edit.as_view(), name="edit"), 
     path('client-delete/<pk>/', Client_delete.as_view(), name="delete"),
     #-------------------------------------------------------------
     path('login/', login_request, name = "login"),
     path('register/', register, name = "register"),
     path('logout/', LogoutView.as_view(template_name='logout.html'), name = "logout")
]
