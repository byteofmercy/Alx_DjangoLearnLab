import django
import os

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Library, Book, Author

# 1. List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # <- important line
    books = library.books.all()
    for book in books:
        print(book.title)

# 2. Query all books by a specific author
def list_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(book.title)

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(library.librarian)


# Run sample queries when this file is executed
if __name__ == "__main__":
    print("Books in Central Library:")
    list_books_in_library("Central Library")

    print("\nBooks by J.K. Rowling:")
    list_books_by_author("J.K. Rowling")

    print("\nLibrarian for Central Library:")
    get_librarian_for_library("Central Library")
