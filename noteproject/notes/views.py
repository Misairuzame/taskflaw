from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.
def noteList(request):
    return HttpResponse("This is where my notes are.")

def index(request):
    return HttpResponse("Hello, world. You're at the notes index.")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})