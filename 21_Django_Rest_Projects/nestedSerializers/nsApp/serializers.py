from nsApp.models import Author,Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

# We'll first create Author and then the books, so chose read_only for books here
class AuthorSerializer(serializers.ModelSerializer):
    books=BookSerializer(read_only=True,many=True)  # default is read_only=False
    class Meta:
        model=Author
        fields='__all__'
