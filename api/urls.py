from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes, name='routes'),
    path('authors/', views.getAuthors, name='authors'),
    path('authors/<int:id>/', views.getAuthor, name='author'),
    path('publishers/', views.getPublishers, name='publishers'),
    path('publishers/<int:id>/', views.getPublisher, name='publisher'),
    path('book_catagories/', views.getBookCatagories, name='book_catagories'),
    path('child_book_catagories/<int:id>/', views.getChildBookCatagories, name='child_book_catagories'),
    path('books/', views.getBooks, name='books'),
    path('books/<int:id>/', views.getBook, name='book'),
]
