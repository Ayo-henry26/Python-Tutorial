from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return redirect('/loginn')
        
    return render(request, 'blog/loginn.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'blog/signup.html')


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def newpost(request):
    
    return render(request, 'blog/newpost.html')


def mypost(request):
    return render(request, 'blog/mypost.html')


def signout(request):
    return render(request, 'blog/signout.html')