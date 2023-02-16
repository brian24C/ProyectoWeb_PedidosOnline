from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.

def blog (request):

    posts=Post.objects.all()
    return render(request, "blogT/blog.html", {"posts":posts})  

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    
    posts=Post.objects.filter(categorias=categoria_id)    #también puede ser categorias=categoria_id

    return render(request, "blogT/categorias.html", {"categoria":categoria,"posts":posts})
    