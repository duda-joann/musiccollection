from django.urls import path
from .views import AlbumListView, FormAlbumView, ArtistView, ThanksView, UpdateAlbum, DeleteAlbum, OwnAlbumsView



app_name = 'musiccollection'

urlpatterns = [
    path('albums/', AlbumListView.as_view(), name="albums"),
    path('addnew/', FormAlbumView.as_view(), name="new"),
    path('newartist/', ArtistView.as_view(), name="newartist"),
    path('thanks/', ThanksView.as_view(), name="thanks"),
    path('update/<title>', UpdateAlbum.as_view(), name="update"),
    path('delete/<title>', DeleteAlbum.as_view(), name="delete"),
    path('addtomycollection/<album>', OwnAlbumsView.as_view(), name = "addfav")
]