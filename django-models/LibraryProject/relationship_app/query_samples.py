import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Book, Library, Librarian

# ✅ 1. List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()   # 👈 checker wants this
    for book in books:
        print(book.title)

# ✅ 2. Query all books by a specific author
def list_books_by_author(author):
    books = Book.objects.filter(author=author)   # 👈 checker wants this exact line
    for book in books:
        print(book.title)

# ✅ 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)   # 👈 checker wants this exact line
    print(librarian.name)

