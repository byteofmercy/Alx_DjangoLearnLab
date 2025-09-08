from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# Show all books (with their authors)
class BookListView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"

# Show details for a specific library (with books and librarian)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
