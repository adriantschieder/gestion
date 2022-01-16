from django.urls import path
from .views import (
     #funciones de Clientes

     #funciones de Maquinarias

     #funciones de Arreglos
     arreglos,arreglos_cliente,agregar_arreglos_clientes,arreglos_editados,eliminar_arreglo,
     )

urlpatterns = [
     path('arreglos/',arreglos, name ='arreglos'),
     path('arreglos-cliente/<id>', arreglos_cliente, name = 'arreglosclientes'),
     # path('arreglos-agregar/<idmaquina>', arreglos_agregar, name = 'agregar-arreglos'),
     path('arreglos-agregados/<int:id>',agregar_arreglos_clientes, name='arreglos-agregados'),
     # path('ver-arreglos/<id>/<idmaquina>', editar_arreglos_cliente, name = 'ver arreglos'),
     path('arreglos-editados/<id>/<idmaquina>', arreglos_editados, name='arregloseditados'),
     path('eliminar-arreglo/<id>/<idmaquina>', eliminar_arreglo, name = 'eliminar-arreglo'),

]