from django.urls import path
from .views import (
     #funciones de Clientes

     #funciones de Maquinarias
     maquinarias,agregar_maquinas,

     #funciones de Arreglos
     arreglos,arreglos_cliente,agregar_arreglos_clientes,arreglos_editados,eliminar_arreglo,
     )

urlpatterns = [
     path('arreglos/',arreglos, name ='arreglos'),
     path('arreglos-cliente/<id>', arreglos_cliente, name = 'arreglosclientes'),
     path('arreglos-agregados/<int:id>',agregar_arreglos_clientes, name='arreglos-agregados'),
     path('arreglos-editados/<id>/<idmaquina>', arreglos_editados, name='arregloseditados'),
     path('eliminar-arreglo/<id>/<idmaquina>', eliminar_arreglo, name = 'eliminar-arreglo'),
     #------------------------------------------------------------
     path ("maquinarias/", maquinarias, name = "maquinarias"),
     path ("agregar_maquinarias/", agregar_maquinas)
]