from django.contrib import admin
from .models import Post,Comentario, Contacto
# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Contacto)