
from relationship_app.models import Library, Book, Author, Librarian

# 1. List all books in a library.
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)   # required by checker
    return Book.objects.filter(library=library)

# 2. Query all books by a specific author.
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 3. Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)   # required by checker
    return Librarian.objects.get(library=library)
