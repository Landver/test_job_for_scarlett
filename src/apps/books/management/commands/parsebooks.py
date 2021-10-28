from django.core.management.base import BaseCommand

from apps.books.services.parser import BookParse


BASE_URL = "https://thegreatestbooks.org/the-greatest-fiction-since"


class Command(BaseCommand):
    help = 'Parse books and save them to DB'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Processing... 🚀'))

        BookParse(f'{BASE_URL}/2010')
        BookParse(f'{BASE_URL}/2000')
        BookParse(f'{BASE_URL}/1990')
        BookParse(f'{BASE_URL}/1980')
        BookParse(f'{BASE_URL}/1970')
        BookParse(f'{BASE_URL}/1900')

        self.stdout.write(self.style.SUCCESS('Successfully parsed products 🎉'))
