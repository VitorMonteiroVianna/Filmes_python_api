from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmnin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date', 'resume']