from unicodedata import name
from django.urls import path
from .views import NoteList, NoteDetail

urlpatterns = [
    path('', NoteList.as_view(), name='notes'),
    path('note/<int:pk>/', NoteDetail.as_view(), name='note'),
]