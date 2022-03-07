from django.db import models

# Create your models here.
class Note(models.Model):
    note_text = models.CharField(max_length=200)