from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import BookSerializer


# Create your views here.


class BookListView(generics.ListCreateAPIView):
    # Book.generate_fake_data()
    model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Book created successfully'}, status=status.HTTP_201_CREATED)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        bookId = kwargs['bookId']
        return Response({'message': f'Book {bookId} updated successfully', 'bookId': bookId}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        bookId = kwargs['bookId']
        return Response({'message': f'Book {bookId} deleted successfully', 'bookId': bookId},
                        status=status.HTTP_204_NO_CONTENT)
