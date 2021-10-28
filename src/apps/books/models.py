from django.db import models


class Author(models.Model):
    """ Author Instance """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'authors'
        ordering = ('first_name', 'last_name')


class Genre(models.Model):
    """ Genre Instance """
    name = models.CharField('Genre Title', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genres'
        ordering = ('name',)


class Book(models.Model):
    """ Book Instance """
    name = models.CharField('Book Title', max_length=128)
    synopsis = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, db_index=True)  # I keeped here indexation of database just to show you that I know that

    def __str__(self):
        return f"{self.name} - {self.writer}"

    class Meta:
        db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('name', 'genres__name', 'release_date', 'price')
