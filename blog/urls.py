from django.urls import path
from .views import  homeview, postdetailview,nuevo_blog

urlpatterns = [

path("agregar_post/", nuevo_blog.as_view(), name = "agregar_post"),
path("", homeview.as_view(), name = "home"),
path ("post/<int:pk>", postdetailview.as_view(), name="post_detail")







]