from pyexpat import model
from tkinter import CASCADE
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=255, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cuerpo = models.TextField()


    def __str__(self):
        return self.titulo + "/" + str(self.autor)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})