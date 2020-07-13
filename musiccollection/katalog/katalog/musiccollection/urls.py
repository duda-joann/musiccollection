from django.urls import path
from .views import AlbumListView, FormAlbumView, ArtistView, ThanksView, UpdateAlbum, DeleteAlbum


app_name = 'musiccollection'

urlpatterns = [
    path('albums/', AlbumListView.as_view(), name="albums"),
    path('addnew/', FormAlbumView.as_view(), name="new"),
    path('newartist/', ArtistView.as_view(), name="newartist"),
    path('thanks/', ThanksView.as_view(), name="thanks"),
    path('update/<pk>', UpdateAlbum.as_view(), name="update"),
    path('<pk>/delete/', DeleteAlbum.as_view(), name="delete")
]