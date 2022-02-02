from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Perfil_Usuario(models.Model):
    usuario= models.OneToOneField(User, primary_key=id, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    ciudad = models.CharField(max_length=100,null=True,blank=True)
    provincia = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.IntegerField(null=True,blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True,blank=True,default='avatar/avatar.png')

def createProfile(sender, instance, created, **kwargs):
    if created:
        Perfil_Usuario.objects.create(usuario=instance)
post_save.connect(createProfile, sender=User)