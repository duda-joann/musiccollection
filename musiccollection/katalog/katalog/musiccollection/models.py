from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    genre = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{str(self.genre)}'


class Album(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    RATING_CHOICES = {
        (ONE, "★"),
        (TWO, "★★"),
        (THREE, "★★★"),
        (FOUR, "★★★★"),
        (FIVE, "★★★★★")}

    title = models.CharField(max_length=100)
    band = models.OneToOneField('Artist', related_name='+', on_delete=models.CASCADE, default=0)
    the_year_of_publishment = models.DateTimeField(null=True, blank=True)
    cover = models.ImageField(upload_to='album/covers', max_length=500, null=True, blank=True)
    ean = models.CharField(max_length=100, unique=True, null=True, blank=True)
    kat_nr = models.CharField(max_length = 100, null=True, blank=True)
    country_of_issued_of_album = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500, null=True, blank=True)
    rating = models.CharField(max_length=10, default=5, choices=RATING_CHOICES)
    genre = models.ManyToManyField(Genre)

    def format(self):
        return f'{str(self.title)} + " " + ({str(self.the_year_of_publishment)})'

    def __str__(self):
        return self.format()

    class Meta:
        verbose_name = 'album'
        ordering = ["-the_year_of_publishment"]
        unique_together = ['title', 'band']


class Artist(models.Model):
    name = models.CharField(max_length=200)
    country_of_origin = models.CharField(max_length=200, blank=True, null=True)
    foundation_year = models.DateTimeField()
    genre = models.ManyToManyField(Genre)
    album = models.ManyToManyField(Album, blank=True)

    def format(self):
        return f'{str(self.name)}({str(self.country_of_origin)})'

    def __str__(self):
        return self.format()

    class Meta:
        unique_together = ['name', 'country_of_origin']


class MusicLabel(models.Model):
    music_label = models.ManyToManyField(Album)

    def format(self):
        return f'{str(self.music_label)}'

    def __str__(self):
        return self.format()


class MyCollection(models.Model):
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    album = models.ManyToManyField(Album)
    add_date = models.DateTimeField(default=timezone.now)

    def format(self):
        return f'{str(self.owner)}, {str(self.album)}'

    def __str__(self):
        return self.format()
