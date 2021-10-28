from rest_framework import serializers
from apps.books.models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    """ Author Instance Serializer """
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """ Genre Instance Serializer """
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """ Book Instance Serializer """
    class Meta:
        model = Book
        fields = '__all__'


class CustomBookSerializer(serializers.ModelSerializer):
    """ Book Instance Serializer """
    writer = AuthorSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
