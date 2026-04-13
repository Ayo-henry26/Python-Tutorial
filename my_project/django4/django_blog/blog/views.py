from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginn(request):
    return render(request, 'blog/loginn.html')

def signup(request):
    return render(request, 'blog/signup.html')

def home(request):
    return render(request, 'blog/home.html')

def newpost(request):
    return render(request, 'blog/newpost.html')

def mypost(request):
    return render(request, 'blog/mypost.html')

def signout(request):
    return render(request, 'blog/signout.html')