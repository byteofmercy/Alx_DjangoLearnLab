import os
import sys
import django

# -------------------------------
# 1. Setup Django environment
# -------------------------------

# Get the absolute path to the project folder (where manage.py is)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Tell Django where settings.py is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# -------------------------------
# 2. Import our models
# -------------------------------
from relationship_app.models import Author, Book, Library, Librarian

# -------------------------------
# 3. Sample queries
# -------------------------------

# 1. Query all books by a specific author
author_name = "John Doe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print("-", book.title)
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian found for {library_name}")

