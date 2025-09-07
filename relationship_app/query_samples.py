from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    for author in authors:
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)

# List all books in a library
def books_in_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    for library in libraries:
        books = library.books.all()
        for book in books:
            print(book.title)

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    for library in libraries:
        librarian = Librarian.objects.filter(library=library)
        for l in librarian:
            print(l.name)
