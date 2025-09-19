
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# 🔒 Secure view with permission check
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # ORM prevents SQL injection
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example form view with CSRF protection
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # handle safe data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
