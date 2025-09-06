
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    # FIX: added related_name="books" so we can use author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

=======
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(default=2024)
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, blank=True)
>>>>>>> ead0755 (Second project: Django Views and URL Configuration)
    def __str__(self):
        return self.name
