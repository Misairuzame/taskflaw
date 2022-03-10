from unicodedata import name
from django.urls import path
from .views import NoteList, NoteDetail, NoteCreate

urlpatterns = [
    path('', NoteList.as_view(), name='notes'),
    path('note/<int:pk>/', NoteDetail.as_view(), name='note'),
    path('note-create/', NoteCreate.as_view(), name='note-create'),
]