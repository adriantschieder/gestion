from django.urls import path

from .views import  inicio_blog, postdetailview,nuevo_blog,actualizar_post,BorrarPost,LikeView, Agregar_comentario

urlpatterns = [

path("agregar_post/", nuevo_blog.as_view(), name = "agregar_post"),
path("", inicio_blog.as_view(), name = "home"),
path ("post/<int:pk>", postdetailview.as_view(), name="post_detail"),
path( "post/edit/<int:pk>", actualizar_post.as_view(), name= "actualizar_post"),
path( "post/<int:pk>/eliminar", BorrarPost.as_view(), name= "eliminar_post"),
path( "like/<int:pk>", LikeView, name= "like"),
path("post/<int:pk>/comentario", Agregar_comentario.as_view(), name= "crear_comentario")
]