from django.urls import path
from .views import (AlbumListView,
                    FormAlbumView,
                    ArtistView,
                    ThanksView,
                    UpdateAlbum,
                    DeleteAlbum,
                    add_to_own_albums,
                    remove_from_my_collections,
                    CollectionListView)


app_name = 'musiccollection'

urlpatterns = [
    path('album/<slug>', AlbumListView.as_view(), name="album"),
    path('addnew/', FormAlbumView.as_view(), name="new"),
    path('newartist/', ArtistView.as_view(), name="newartist"),
    path('thanks/', ThanksView.as_view(), name="thanks"),
    path('update/<slug>', UpdateAlbum.as_view(), name="update"),
    path('delete/<slug>', DeleteAlbum.as_view(), name="delete"),
    path('my-collection', CollectionListView.as_view(), name ="Collection"),
    path('add-to-my-collection/<slug>', add_to_own_albums, name = "add-to-my-collection"),
    path('remove-from-my-collection/<slug>', remove_from_my_collections, name="remove-from-my-collection")

]