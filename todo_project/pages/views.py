from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CreateUser(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = CreateUser()
    return render(request, 'pages/register.html', {"form": form})

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or Password is incorrect")
    
    return render(request, 'pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
