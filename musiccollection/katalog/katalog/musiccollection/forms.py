from django import forms
from .models import Album, Artist, MyCollection


class FormAlbum(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'band', 'the_year_of_publishment', 'cover', 'ean', 'kat_nr',
                  'description', 'country_of_issued_of_album', 'rating', 'genre')


class FormArtist(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'country_of_origin', 'foundation_year', 'genre')


class FormMyCollection(forms.ModelForm):

    class Meta:
        model = MyCollection
        fields = ['album']