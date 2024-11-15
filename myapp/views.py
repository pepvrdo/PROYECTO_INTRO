from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def principal(request):
    return render(request, 'index.html')

def noauth(request):
    return render(request, 'home0.html')

def home(request):
    return render(request, 'home.html')

def respiracion(request):
    return render(request, 'respiracion.html')

def about(request):
    return render(request, 'about.html')

def signout(request):
    logout(request)
    return redirect("home0")