from django.urls import path
from .views import bandeja, borrar, enviados, leerenviados, leermail, profile, list_user, redactar, redactarmail


urlpatterns = [
     path('perfil/<id>',profile, name ='perfil'),
     path('list-user/', list_user, name="list-user"),
     path('leer/<id>', leermail, name="leermail"),
     path('leerenviados/<id>', leerenviados, name="leerenviados"),
     path('bandeja/', bandeja, name="bandeja"),
     path('redactar/', redactarmail, name="redactar"),
     path('redactar_usuario/<id>', redactar, name="redactarusuario"),
     path('enviados/', enviados, name="enviados"),
     path('borrar/<id>', borrar, name="borrar"),
]