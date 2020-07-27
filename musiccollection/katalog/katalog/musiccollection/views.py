from django.views.generic import ListView, FormView, TemplateView, DeleteView, UpdateView, CreateView
from .models import Album, Artist, MusicLabel, Genre
from .forms import FormAlbum, FormArtist, FormMyCollection
# Create your views here.


class MainPage(TemplateView):
    template_name = 'musiccollection/main.html'


class ThanksView(TemplateView):
    template_name = 'musiccollection/thanks.html'


class AlbumListView(ListView):
    template_name = 'musiccollection/album.html'
    model = Album
    context_object_name = 'albums'
    paginate_by = 10
    ordering = ['-created']


class ArtistListView(ListView):
    template_name = 'all_artist.html'
    model = Artist
    context_object_name = 'artist'
    paginate_by = 10
    ordering = ['name']


class FormAlbumView(FormView):
    template_name = 'musiccollection/add_new.html'
    form_class = FormAlbum
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class ArtistView(FormView):
    template_name = 'musiccolecction/artist_new.html'
    form_class = FormArtist
    success_url = '/thanks/'

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateAlbum(UpdateView):
    form_class = FormAlbum
    template_name = 'musiccollection/update.html'
    success_url = '/albums/'

    def get_object(self, queryset=None):
        object_to_update = Album.objects.get(title=self.kwargs['title'])
        return object_to_update


class DeleteAlbum(DeleteView):
    model = Album
    template_name = "musiccollection/delete.html"
    success_url = '/albums/'

    def get_object(self, queryset=None):
        object_to_update = Album.objects.get(title=self.kwargs['title'])
        return object_to_update


class OwnAlbumsView(CreateView):
    template_name = 'musiccollection/add_to_fav.html'
    form_class = FormMyCollection
    success_url = '/albums/'

    def get_object(self, queryset=None):
        object_to_save = Album.objects.get(title=self.kwargs['title'])
        return object_to_save

    def save(self):
        album = self.get_object()
        FormMyCollection.save(album)

