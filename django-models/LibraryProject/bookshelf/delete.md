from bookshelf.models import Book

## Delete
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
print(books)

# Output:
# (1, {'bookshelf.Book': 1})
# <QuerySet []>
