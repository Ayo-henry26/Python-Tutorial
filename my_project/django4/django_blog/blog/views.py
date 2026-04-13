from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginn(request):
    return render(request, 'blog/loginn.html')

def signup(request):
    return render(request, 'blog/signup.html')

def home(request):
    return render(request, 'blog/home.html')