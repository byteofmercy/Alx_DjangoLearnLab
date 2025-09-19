from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view book list"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"



