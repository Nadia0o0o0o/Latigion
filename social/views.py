from django.shortcuts import render
from .models import Post


def social_home(request):
    return render(request, 'social/social_home.html')



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/feed.html', {'posts': posts})


def plantilla_no_funciona(request):
    return render(request, 'social/plantilla_no_funciona.html')
