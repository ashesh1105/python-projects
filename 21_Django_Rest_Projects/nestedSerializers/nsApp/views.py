# Need these if you want to use viewsets
# from nsApp.models import Author, Book
# from nsApp.serializers import AuthorSerializer,BookSerializer
# from rest_framework import viewsets

from nsApp.models import Author,Book
from nsApp.serializers import AuthorSerializer,BookSerializer
from rest_framework import generics

# Create your views here.
# Author view
# Need below if you want to use viewsets. Note urls.py will be different then.
# Check project: cbvSerializers to see details!
'''
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
'''

class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class = AuthorSerializer

# Book view
# Need below if you want to use viewsets. Note urls.py will be different then.
# Check project: cbvSerializers to see details!
'''
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
'''

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer
