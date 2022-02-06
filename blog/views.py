
from re import template
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import Postform

# Create your views here.


class homeview(ListView):
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
