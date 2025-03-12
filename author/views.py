from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import AuthorProfile


def author_home(request):
    return render(request, 'author/author_home.html')
    
def dibujo(request):
    return render(request, 'author/dibujo.html')


def writer(request):
    return render(request, 'author/script_writer.html')


def tutorial(request):
    return render(request, 'author/tutorials.html')


def herramientas_creativas(request):
    return render(request, 'author/Herramientas_creativas.html')

def blog(request):
    return render(request, 'author/blog_1.html')