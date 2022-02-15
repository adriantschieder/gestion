from email.policy import default
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime, date


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=255, default="titulo")
    subtitulo = models.CharField(max_length=255, default = "subtitulo")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    cuerpo = RichTextField(blank=True, default = "cuerpo")
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    portada_post = models.ImageField(upload_to="portadas_post", null = True)
    me_gusta = models.ManyToManyField(User, related_name = "blog_post" )

    def __str__(self):
        return self.titulo + "/" + str(self.autor)

    def get_absolute_url(self):
        #return reverse('post_detail', kwargs={'pk': self.pk})
        return reverse("home")

    def  total_likes(self):
        return self.me_gusta.count()




class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cuerpo = RichTextField()
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return "%s- %s" % (self.post.titulo, self.cuerpo)



class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    numero_telefono = models.IntegerField()
    email = models.EmailField()
    cuerpo = RichTextField()