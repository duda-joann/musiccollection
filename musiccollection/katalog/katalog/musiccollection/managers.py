from django.db import models


class GenreManager(models.Manager):

    def queryset(self, genre):
        return super().get_queryset().filter(genre=self.genre)


