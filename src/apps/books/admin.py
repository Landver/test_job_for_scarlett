from django.contrib import admin
from .models import Author, Book, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'writer', 'price', 'genres_display')
    list_filter = ('release_date', 'genres')
    search_fields = ('name', 'writer', 'genres')

    def genres_display(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
