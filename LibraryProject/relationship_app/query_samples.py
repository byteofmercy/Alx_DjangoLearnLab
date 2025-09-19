import os
import django

# setup Django so we can run this file directly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# SAMPLE DATA (optional if you already created in admin)
author = Author.objects.create(name='John Doe')
book1 = Book.objects.create(title='Book One', author=author)
book2 = Book.objects.create(title='Book Two', author=author)

library = Library.objects.create(name='Central Library')
library.books.add(book1, book2)

librarian = Librarian.objects.create(name='Jane Smith', library=library)

# 1) Query all books by a specific author
print("Books by John Doe:")
for book in Book.objects.filter(author=author):
    print("-", book.title)

# 2) List all books in a library
print("\nBooks in Central Library:")
for book in library.books.all():
    print("-", book.title)

# 3) Retrieve the librarian for a library
print("\nLibrarian for Central Library:")
print(library.librarian.name)
