from re import search
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Note


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')


class RegisterPage(FormView):
    template_name = 'notes/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegisterPage, self).get(*args, **kwargs)


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        context['count'] = context['notes'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:

            # context['notes'] = context['notes'].filter(
            #    title__startswith=search_input)
            # Directly use raw SQL query without sanitization
            context['notes'] = Note.objects.raw(
                f"SELECT * FROM notes_note WHERE user_id = {self.request.user.id}"
                f" AND title LIKE '{search_input}%'"
            )

        context['search_input'] = search_input

        return context


# Remove LoginRequiredMixin in order to introduce the BAC vulnerability
class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note.html'


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('notes')


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')
