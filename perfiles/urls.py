from django.urls import path
from .views import profile, list_user


urlpatterns = [
     path('perfil/<id>',profile, name ='perfil'),
     path('list-user/', list_user, name="list-user"), 
]