from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Author, Publisher, BookCatagory, Book
from api.serializers import AuthorSerializer, PublisherSerializer, BookCatagorySerializer, BookSerializer


@api_view(['GET'])
def getRoutes(request):
    """Get all available API routes."""
    return Response([
        '/api/routes/',
        'api/authors/',
        'api/authors/<int:id>/'
        'api/publishers/',
        'api/publishers/<int:id>/',
        'api/book_catagories/',
        'api/child_book_catagories/<int:id>/'
        'api/books/',
        'api/books/<int:id>/'
    ])


@api_view(['GET'])
def getAuthors(request):
    """Get all authors."""
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAuthor(request, id):
    """Get a specific author."""
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPublishers(request):
    """Get all publishers."""
    publishers = Publisher.objects.all()
    serializer = PublisherSerializer(publishers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPublisher(request, id):
    """Get a specific publisher."""
    try:
        publisher = Publisher.objects.get(pk=id)
    except Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublisherSerializer(publisher, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getBookCatagories(request):
    """Get all catagories."""
    catagories = BookCatagory.objects.all()
    serializer = BookCatagorySerializer(catagories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getChildBookCatagories(request, id):
    """Get all the childs of a catagory."""
    if id == 0:
        id = None
    catagories = BookCatagory.objects.filter(parent=id)
    serializer = BookCatagorySerializer(catagories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBooks(request):
    """Get all books."""
    publishers = Book.objects.all()
    serializer = BookSerializer(publishers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, id):
    """Get a specific book.."""
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
