from django.contrib import admin
from .models import Clientes, Maquinarias, Arreglo_Maquinarias
from blog.models import Post


    
    
    
  

admin.site.register(Clientes)
admin.site.register(Maquinarias)
admin.site.register(Arreglo_Maquinarias)
admin.site.register(Post)

