from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# --------------------------
# Project 1: Books & Libraries
# --------------------------

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --------------------------
# Project 2: User Authentication
# --------------------------

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'relationship_app/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view using built-in class
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using built-in class
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
