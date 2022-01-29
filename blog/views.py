
from re import template
from .models import Post

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


