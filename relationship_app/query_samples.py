import os, sys, django
from pathlib import Path

# setup
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# put some toys inside the box
a = Author.objects.create(name="Chinua Achebe")
b1 = Book.objects.create(title="Things Fall Apart", author=a)
b2 = Book.objects.create(title="No Longer at Ease", author=a)
lib = Library.objects.create(name="City Library")
lib.books.add(b1, b2)
Librarian.objects.create(name="Ms. Wanjiku", library=lib)

# play:
print("Books by Chinua Achebe:", [book.title for book in a.books.all()])
print("Books in City Library:", [book.title for book in lib.books.all()])
print("Librarian for City Library:", lib.librarian.name)
