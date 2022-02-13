


from re import template
from urllib import request

from django.urls import reverse_lazy, reverse
from .models import Post, Comentario
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .forms import Postedit, Postform, Crear_comentario
from django.http import HttpResponseRedirect

# Create your views here.


class inicio_blog(ListView):
    model= Post
    template_name = "home.html"
    ordering = ["-fecha_publicacion"]

class postdetailview(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(postdetailview, self).get_context_data(*args, **kwargs)
        stuff= get_object_or_404(Post, id = self.kwargs["pk"])
        total_likes = stuff.total_likes()

        context["total_likes"] = total_likes
        return context

class nuevo_blog(CreateView):
    model = Post
    form_class = Postform
    template_name = "crear_post.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(nuevo_blog, self).form_valid(form)


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


def LikeView(request, pk):
    post = get_object_or_404(Post, id =request.POST.get("post_id"))
    post.me_gusta.add(request.user)
    return HttpResponseRedirect(reverse("post_detail", args= [str(pk)]))




class Agregar_comentario(CreateView):
    model = Comentario
    form_class = Crear_comentario
    template_name = "agregar_comentario.html"
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.autor = self.request.user
        return super().form_valid(form)
    #def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(Agregar_comentario, self).form_valid(form)
    success_url = reverse_lazy("home")
    


    