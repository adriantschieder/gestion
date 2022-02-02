from django.urls import path
from .views import profile


urlpatterns = [
     path('perfil/<id>',profile, name ='perfil'),
]