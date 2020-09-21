from django.views.generic import ListView, FormView, TemplateView, DeleteView, UpdateView
from .models import Album, Artist, MusicLabel, Genre, MyCollection
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormAlbum, FormArtist, FormMyCollection
from django.contrib.auth.mixins import LoginRequiredMixin


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

    def form_valid (self, form):
        return super().form_valid(form)


class ArtistView(FormView):
    template_name = 'musiccolecction/artist_new.html'
    form_class = FormArtist
    success_url = '/thanks/'

    def form_valid (self, form):
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

    def get_object (self, queryset=None):
        object_to_update = Album.objects.get(title=self.kwargs['title'])
        return object_to_update


class CollectionListView(ListView, LoginRequiredMixin):
    template_name = 'musiccollection/user_collection.html'
    model = MyCollection
    context_object_name = 'albums'
    paginate_by = 10
    ordering = ['-add_date']

    def get_object(self, queryset=None):
        object_to_review = Album.objects.filter(owner=self.request.user)
        return object_to_review


def add_to_own_albums(request, slug):
    item = get_object_or_404(Album, slug)
    own_album, add_date = MyCollection.objects.get_or_create(
        item=item,
        user=request.user,
    )
    my_collection = MyCollection.objects.filter(owner=request.user)
    if my_collection.filter(item__slug=item.slug).exists:
        messages.info(request, "You have got this album in your collection")
        return redirect("mediafinder:album")
    else:
        my_collection.add(own_album)
        messages.info("You added album to your collection")
        return redirect("mediafinder:my-collection")


def remove_from_my_collections(request, slug):
    pass