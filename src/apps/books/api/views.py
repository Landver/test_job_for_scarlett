from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.books.models import Book
from .serializers import BookSerializer, CustomBookSerializer


class CommonMethods():
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        ''' customized original function of DRF. You need it for proper POST/PUT/PATCH requests '''
        super().get_serializer_class()

        if self.request.method == 'GET':
            return CustomBookSerializer
        else:
            return self.serializer_class


class BookListAPIView(CommonMethods, ListCreateAPIView):
    """ Book List API """
    search_fields = ('name', 'writer__first_name', 'writer__last_name')
    filterset_fields = ['price', 'genres', 'genres__name']


class BookDetailAPIView(CommonMethods, RetrieveUpdateDestroyAPIView):
    """ Book Detail API """
    pass
