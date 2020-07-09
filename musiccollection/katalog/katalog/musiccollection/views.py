from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Album, Artist, MusicLabel, Genre
from .managers import GenreManager
# Create your views here.


class AlbumListView(ListView):
    template_name = 'album.html'
    model = Album
    context_object_name = 'album'
    paginate_by = 10
    ordering = ['-created']

