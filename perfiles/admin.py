from django.contrib import admin

from perfiles.models import MensajeriaInterna, Perfil_Usuario

# Register your models here.
admin.site.register(Perfil_Usuario),
admin.site.register(MensajeriaInterna),