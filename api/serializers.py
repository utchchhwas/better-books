from rest_framework import serializers
from api.models import Author, Publisher, BookCatagory, Book, BookAuthor


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author."""
    class Meta:
        model = Author
        fields = ['id', 'name', 'image']


class PublisherSerializer(serializers.ModelSerializer):
    """Serializer for Publisher."""
    class Meta:
        model = Publisher
        fields = ['id', 'name']

  
class BookCatagorySerializer(serializers.ModelSerializer):
    """Serializer for BookCatagory."""
    catagory_list_from_root = serializers.ListField(source='getListFromRoot')

    class Meta:
        model = BookCatagory
        fields = ['id', 'catagory_list_from_root']


class BookAuthorSerializer(serializers.ModelSerializer):
    """Serializer for BookAuthor."""
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = BookAuthor
        fields = ['author', 'rank']


class BookSerializer(serializers.ModelSerializer):
    """Serializer for Book."""
    authors = BookAuthorSerializer(source='bookauthor_set', many=True, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)
    catagories = BookCatagorySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['isbn',
                  'name',
                  'qualified_name',
                  'authors', 
                  'edition', 
                  'publication_year', 
                  'language', 
                  'country', 
                  'number_of_pages', 
                  'cover_page', 
                  'publisher', 
                  'catagories', 
                  'additional_info'
        ]
