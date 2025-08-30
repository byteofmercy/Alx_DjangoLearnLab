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



