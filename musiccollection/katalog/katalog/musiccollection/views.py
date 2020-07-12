from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView, DeleteView, UpdateView
from .models import Album, Artist, MusicLabel, Genre
from .forms import FormAlbum, FormArtist
from .managers import GenreManager
# Create your views here.


class ThanksView(TemplateView):
    template_name = 'thanks.html'


class AlbumListView(ListView):
    template_name = 'album.html'
    model = Album
    context_object_name = 'album'
    paginate_by = 10
    ordering = ['-created']


class FormAlbumView(FormView):
    template_name = 'add_new.html'
    form_class = FormAlbum
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class ArtistView(FormView):
    template_name = 'artist_new.html'
    form_class = FormArtist
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateAlbum(UpdateView):
    pass


class DeleteAlbum(DeleteView):
    pass 