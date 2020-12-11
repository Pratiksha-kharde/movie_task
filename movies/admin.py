from django.contrib import admin

from .models import Movie, GenreData
# Register your models here.
admin.site.register(Movie)
admin.site.register(GenreData)
