import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = [book.title for book in library.books.all()]
print(f"Books in {library_name}: {books_in_library}")

# Query all books by a specific author
author_name = "Author A"
author = Author.objects.get(name=author_name)
books_by_author = [book.title for book in author.books.all()]
print(f"Books by {author_name}: {books_by_author}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library_name}: {librarian.name}")
