import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation ---
# Create authors
author_a, created = Author.objects.get_or_create(name="Author A")
author_b, created = Author.objects.get_or_create(name="Author B")

# Create books
book1, created = Book.objects.get_or_create(title="Book 1", author=author_a)
book2, created = Book.objects.get_or_create(title="Book 2", author=author_a)
book3, created = Book.objects.get_or_create(title="Book 3", author=author_b)

# Create library
library, created = Library.objects.get_or_create(name="Central Library")
library.books.set([book1, book2, book3])  # Add books to library

# Create librarian
librarian, created = Librarian.objects.get_or_create(name="Mr. Smith", library=library)

# --- Queries ---
# 1. Query all books by a specific author
books_by_author_a = Book.objects.filter(author=author_a)
print("Books by Author A:", [book.title for book in books_by_author_a])

# 2. List all books in a library
books_in_library = library.books.all()
print("Books in Central Library:", [book.title for book in books_in_library])

# 3. Retrieve the librarian for a library
librarian_of_library = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian_of_library.name)

