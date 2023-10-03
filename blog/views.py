from django.shortcuts import render
from .models import *


# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    post = Post.objects.get( id = id)
    return render(request, 'blog/post.html', {'post':post})

def search(request):
    search_data = request.GET.get('search_data','')

    if search_data:
        qd = Post.objects.filter(title = search_data)
    else:
        qd = Post.objects.all().order_by("-date")
    return render(request, 'blog/blog.html', {
        'posts': qd,
        'search_data': search_data,
    })

def next_post(request, id):
    current_post = Post.objects.get(id=id)
    next_post = Post.objects.filter(id__gt=id).order_by('id').first()
    return render(request, 'blog/next_post.html', {'next_post': next_post})


