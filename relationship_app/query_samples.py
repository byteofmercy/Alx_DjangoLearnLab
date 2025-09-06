import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# List all books in a specific library
library = Library.objects.get(name="City Library")
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(f"- {book.title} by {book.author.name} (Published {book.publication_year})")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
