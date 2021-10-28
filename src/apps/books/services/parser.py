import random
from typing import NamedTuple

from bs4 import BeautifulSoup as BS
import requests

from apps.books.models import Author, Book, Genre


class BookData(NamedTuple):
    """ Book Data Class"""
    name: str
    synopsis: str
    writer: Author
    date: str
    genre: Genre
    price: str


class BookParse:
    """ Book Parser """
    def __init__(self, link):
        self.link = link
        self.date = f"{link.split('/')[-1]}-01-01"
        self.data = self.get_data()
        self._fill_db()

    def get_data(self):
        """ return list of book data from web by parser """
        data = list()
        response = requests.get(self.link)
        soup = BS(response.text, 'lxml')
        div = soup.find('div', class_='list-body')
        for li in div.find_all('li', class_='item'):
            title = li.find('h4')
            name = title.find('a').get_text()
            writer = title.find('a').find_next('a').get_text()
            synopsis = li.find('p').get_text().strip()
            data.append(BookData(
                name=name,
                synopsis=synopsis,
                writer=self._get_or_create_writer(writer),
                date=self.date,
                price=self._random_price(),
                genre=self._random_genre()))
        return data

    def _random_genre(self) -> Genre:
        """ return random genre for book """
        genres = ('Action and Adventure', 'Classics', 'Comic Book or Graphic Novel',
                  'Detective and Mystery', 'Fantasy', 'Historical Fiction',
                  'Horror', 'Literary Fiction', 'Romance', 'Science Fiction (Sci-Fi)',
                  'Short Stories', 'Suspense and Thrillers', "Women's Fiction",
                  "Biographies and Autobiographies", "Cookbooks", "Poetry", "Self-Help")
        name = random.choice(genres)
        return Genre.objects.get_or_create(name=name)[0]

    def _random_price(self):
        price = random.randrange(1, 101)
        return f"{price}.00"

    def _get_or_create_writer(self, writer: str) -> Author:
        """ get or create writer instance """
        if " " in writer:
            first_name, last_name = writer.split(maxsplit=1)
        else:
            first_name = writer
            last_name = " "
        writer = Author.objects.get_or_create(first_name=first_name, last_name=last_name)[0]
        return writer

    def _fill_db(self) -> None:
        """ creation book instance by data from parser """
        for book in self.data:
            book_instance = Book.objects.create(
                name=book.name,
                synopsis=book.synopsis,
                writer=book.writer,
                release_date=book.date,
                price=book.price)
            book_instance.genres.add(book.genre)
            book_instance.save()
        return
