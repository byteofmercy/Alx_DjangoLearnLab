from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

