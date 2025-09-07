# relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Library  # Project 1 models

# -----------------------
# Project 1: Function-based view for listing books
# -----------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -----------------------
# Project 1: Class-based view for library details
# -----------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# -----------------------
# Project 2: User registration view
# -----------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# -----------------------
# Project 2: Login and Logout views
# -----------------------
login_view = LoginView.as_view(template_name='relationship_app/login.html')
logout_view = LogoutView.as_view(template_name='relationship_app/logout.html')

