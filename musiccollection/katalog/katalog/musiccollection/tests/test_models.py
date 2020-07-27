from django.test import TestCase
from ..models import Genre, MusicLabel, Album, Artist


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(
            genre='Heavy Metal')

    def test_genre_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')


class MusicLabelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MusicLabel.objects.create(
            music_label='Elektra Records',
            country='USA',
            foundation_year="1950-01-01")

    def test_music_label(self):
        music_label = MusicLabel.objects.get(id=1)
        field_label = music_label._meta.get_field('music_label').verbose_name
        self.assertEquals(field_label, 'music_label')

    def test_country(self):
        country = MusicLabel.objects.get(id=1)
        country_field_label = country._meta.get_field('country').verbose_name
        self.assertEquals(country_field_label, 'country')

    def test_foundation_year(self):
        music_label = MusicLabel.objects.get(id=1)
        foundation_year_field_label = music_label.meta.get_field('foundation_year').verbose_name
        self.assertEquals(foundation_year_field_label, 'foundation_year')


class AlbumModelTest(TestCase):
    def setUpTestData(cls):
        Album.objects.create(
            title="Kill 'Em All",
            band='Metallica',
            the_year_of_publishment='1985-07-25',
            ean="602547885289",
            kat_nr='4788528',
            country_of_issued_of_album='USA',
            created='2020-07-27',
            description='first Metallica album',
            rating='5',
            genre='thrash metal',
            musiclabel='Elektra Records')

    def test_title_label(self):
        album = Album.objects.get(id=1)
        title_field_label = album._meta.get_field('title').verbose_name
        self.assertEqual(title_field_label, 'title')

    def test_band_label(self):
        album = Album.objects.get(id=1)
        band_field_label = album._meta.get_field('band').verbose_name
        self.assertEqual(band_field_label, 'band')

    def test_the_year_of_publishment_label(self):
        album = Album.objects.get(id=1)
        band_field_label = album._meta.get_field('the_year_of_publishment').verbose_name
        self.assertEqual(band_field_label, 'the_year_of_publishment')

    def test_ean_label(self):
        album = Album.objects.get(id=1)
        ean_field_label = album._meta.get_field('ean').verbose_name
        self.assertEqual(ean_field_label, 'the_year_of_publishment')

    def test_country_of_issued_album_label(self):
        album = Album.objects.get(id=1)
        band_field_label = album._meta.get_field('country_of_issued_of_album').verbose_name
        self.assertEqual(band_field_label, 'the_year_of_publishment')

    def test_created_label(self):
        album = Album.objects.get(id=1)
        created_field_label = album._meta.get_field('created').verbose_name
        self.assertEqual(created_field_label, 'created')

    def test_description_album_label(self):
        album = Album.objects.get(id=1)
        description_field_label = album._meta.get_field('description').verbose_name
        self.assertEqual(description_field_label, 'description')

    def test_rating_album_label (self):
        album = Album.objects.get(id=1)
        rating_field_label = album._meta.get_field('rating').verbose_name
        self.assertEqual(rating_field_label, 'rating')

    def test_genre_label(self):
        album = Album.objects.get(id=1)
        genre_field_label = album._meta.get_field('genre').verbose_name
        self.assertEqual(genre_field_label, 'genre')

    def test_music_label_label(self):
        album = Album.objects.get(id=1)
        music_label_field_label = album._meta.get_field('musiclabel').verbose_name
        self.assertEqual(music_label_field_label, 'the_year_of_publishment')


class ArtistModelTest(TestCase):

    def setUpTestData(cls):
        Artist.objects.create(
            name='Metallica',
            country_of_origin = 'USA',
            album=['Masters Of Puppets', 'Ride The Lightning'],
            biography = 'The most popular band on the world',
            )

    def test_band_name_label(self):
        band = Artist.objects.get(id=1)
        name_label = band._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_country_of_origin_label(self):
        band = Artist.objects.get(id=1)
        country_of_origin_label = band._meta.get_field('country_of_origin').verbose_name
        self.assertEqual(country_of_origin_label, 'country_of_origin')

    def test_album_label(self):
        band = Artist.objects.get(id=1)
        album_label = band._meta.get_field('album').verbose_name
        self.assertEqual(album_label, 'album')

    def test_biography_label(self):
        band = Artist.objects.gest(id=1)
        biography_label = band._meta.get_field('biography').verbose_name
        self.assertEqual(biography_label, 'biography')
