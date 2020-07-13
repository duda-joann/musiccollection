from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Album, Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist

    fields = ['name', 'country_of_origin', 'genre', 'foundation_year',
              'genre', 'album', 'biography', 'photography']
