from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime, date


# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=255, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cuerpo = RichTextField(blank=True,null=True)
    fecha_publicacion= models.DateField(auto_now=True)


    def __str__(self):
        return self.titulo + "/" + str(self.autor)

    def get_absolute_url(self):
        #return reverse('post_detail', kwargs={'pk': self.pk})
        return reverse("home")