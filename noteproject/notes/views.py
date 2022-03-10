from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')

class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note.html'

class NoteCreate(CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('notes')

class NoteUpdate(UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('notes')

class NoteDelete(DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')

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