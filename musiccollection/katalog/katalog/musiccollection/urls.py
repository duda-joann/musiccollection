from django.urls import path
from .views import AlbumListView


app_name = 'musiccollection'

urlpatterns = [
    path('albums/', AlbumListView.as_view(), name = "albums"),
]