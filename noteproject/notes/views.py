from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Note

# Create your views here.
class NoteList(ListView):
    model = Note
    context_object_name = 'notes'

class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note.html'

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