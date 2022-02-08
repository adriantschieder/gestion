
from re import template

from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import Postedit, Postform

# Create your views here.


class inicio_blog(ListView):
    model= Post
    template_name = "home.html"
    ordering = ["-fecha_publicacion"]

class postdetailview(DetailView):
    model = Post
    template_name = "post_detail.html"

class nuevo_blog(CreateView):
    model = Post
    form_class = Postform
    template_name = "crear_post.html"


def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')


class actualizar_post(UpdateView):
    model = Post
    form_class = Postedit
    template_name = "actualizar_post.html"
    

class BorrarPost(DeleteView):
    model = Post
    template_name = "eliminar_post.html"
    success_url = reverse_lazy("home")
