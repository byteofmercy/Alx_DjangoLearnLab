\# CRUD Operations for Book Model



\## Create

```python

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

print(book)

```



\*\*Output:\*\*



```

1984 by George Orwell (1949)

```



\## Retrieve

```python

books = Book.objects.all()

print(books)



book = Book.objects.get(title="1984")

print(book.title, book.author, book.publication\_year)

```



\*\*Output:\*\*



```

<QuerySet \[<Book: 1984 by George Orwell (1949)>]>

1984 George Orwell 1949

```



\## Update

```python

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()

print(book)

```



\*\*Output:\*\*



```

Nineteen Eighty-Four by George Orwell (1949)

```



\## Delete

```python

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()



books = Book.objects.all()

print(books)

```



\*\*Output:\*\*



```

(1, {'bookshelf.Book': 1})

<QuerySet \[]>

```







