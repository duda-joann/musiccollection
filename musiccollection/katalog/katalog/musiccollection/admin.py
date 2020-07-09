from django.contrib import admin
from .models import Album, Artist, MusicLabel, Genre

# Register your models here.

admin.site.register(Album),
admin.site.register(Artist),
admin.site.register(MusicLabel),
admin.site.register(Genre),
