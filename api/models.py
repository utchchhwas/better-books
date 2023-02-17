from django.db import models
import os
from cloudinary.models import CloudinaryField

# Create your models here.

def authorImagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.name}.{ext}'
    return os.path.join('authors/', filename)


class Author(models.Model):
    """Model to represent an author."""
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to=authorImagePath, default=None, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "authors"

    def __str__(self) -> str:
        return self.name
    


class Publisher(models.Model):
    """Model to represent a publisher."""
    name = models.CharField(max_length=100)
        
    class Meta:
        verbose_name_plural = "publishers"

    def __str__(self) -> str:
        return self.name


class BookCatagory(models.Model):
    """Model to represnt hierarchical catagorization of books."""
    catagory = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "book catagories"

    def getListFromRoot(self):
        listFromRoot = []
        curr = self
        while curr is not None:
            listFromRoot.insert(0, (curr.id, curr.catagory))
            curr = curr.parent
        return listFromRoot

    def __str__(self) -> str:
        if self.parent is None:
            return self.catagory
        return self.catagory + ' <- ' + self.parent.__str__()


def bookCoverImagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.name}.{ext}'
    return os.path.join('books/', filename)


class Book(models.Model):
    """Model to represent a book."""
    isbn = models.PositiveBigIntegerField('ISBN', unique=True)
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, through='BookAuthor')
    edition = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    language = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField()
    cover_page = models.ImageField(upload_to=bookCoverImagePath)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    catagories = models.ManyToManyField(BookCatagory)
    additional_info = models.CharField(max_length=100, blank=True)

    @property
    def qualified_name(self):
        return '{}{}'.format(self.name, '' if self.additional_info == '' else f' ({self.additional_info})')
    
    class Meta:
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return self.qualified_name
    

class BookAuthor(models.Model):
    """Intermediate model for Book-Author many-to-many relationship."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural = "book authors"
        constraints = [
                models.UniqueConstraint(fields=['book', 'author'], name='unique book author'),
                models.UniqueConstraint(fields=['book', 'rank'], name='unique book rank'),
        ]

    def __str__(self) -> str:
        return f'{self.rank} - {self.author.name} - {self.book.qualified_name}'
