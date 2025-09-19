# bookshelf/views.py
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookSearchForm, BookForm
from django.db import connection

def book_list(request):
    """
    List books and allow safe searching.
    Uses BookSearchForm to validate input and the ORM to prevent SQL injection.
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            # safe ORM filtering - parameterized internally by Django ORM
            books = books.filter(title__icontains=title)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

def create_book(request):
    """
    Secure form handling for creating a book using ModelForm.
    Always use form.is_valid() and cleaned_data.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # update name if your url name differs
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

def example_raw_query_parametrized(request):
    """
    If you must use raw SQL, ALWAYS use parameterized queries.
    Example shows how to run raw SQL safely.
    """
    title = request.GET.get('title', '')
    if title:
        with connection.cursor() as cursor:
            # DO NOT format strings into SQL. Use parameters (the DB-API will handle quoting).
            cursor.execute("SELECT id, title, author FROM bookshelf_book WHERE title LIKE %s", [f"%{title}%"])
            rows = cursor.fetchall()
            # convert rows to dict or objects as needed
            results = [{'id': r[0], 'title': r[1], 'author': r[2]} for r in rows]
    else:
        results = []
    return render(request, 'bookshelf/raw_results.html', {'results': results})

