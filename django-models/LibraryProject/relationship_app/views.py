# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView   # Must use this exact import for checker
from .models import Library, Book, Author

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

