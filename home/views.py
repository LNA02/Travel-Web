from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from home.forms import BlogPostForm

# Create your views here.
def index(request) :
    return render(request, 'pages/home.html')

def blog(request) :
    return render(request, 'pages/blog.html')

def contact(request):
    return render(request, 'pages/contact.html')
    
def register(request):
    form = RegistrationForm()
    if request.method =='POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect('/')
    
    return render(request, 'pages/register.html', {'form':form})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect("/blog")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'pages/login.html')
    return render(request, "pages/login.html")
     
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/blog')


@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "pages/home.html",{'obj':obj, 'alert':alert})

    else:
        form=BlogPostForm()
    return render(request, "pages/add_blog.html", {'form':form})
