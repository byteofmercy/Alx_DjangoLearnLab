from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    if authors.exists():
        return Book.objects.filter(author__in=authors)
    return []

# 2. List all books in a library
def books_in_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    if libraries.exists():
        return libraries.first().books.all()
    return []

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    if libraries.exists():
        return libraries.first().librarian if hasattr(libraries.first(), "librarian") else None
    return None
