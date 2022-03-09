from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.noteList, name='notes'),
    path('login/', views.login_user, name="login"),
]