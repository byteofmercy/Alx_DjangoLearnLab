import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Library, Book, Author, Librarian

# ------------------------------
# List all books in a library
# ------------------------------
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  # uses related_name='books'
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# ------------------------------
# Query all books by a specific author
# ------------------------------
author_name = "Author A"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# ------------------------------
# Retrieve the librarian for a library
# ------------------------------
librarian = Librarian.objects.get(library=library)
print(f"Librarian of {library_name}: {librarian.name}")
