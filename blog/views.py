
from re import template
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.


class homeview(ListView):
    model= Post
    template_name = "home.html"

class postdetailview(DetailView):
    model = Post
    template_name = "post_detail.html"

class nuevo_blog(CreateView):
    model = Post
    template_name = "crear_post.html"
    fields = "__all__"

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
