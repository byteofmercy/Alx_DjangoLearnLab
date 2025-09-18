# bookshelf/forms.py
from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    """
    Simple search form that validates and cleans user input.
    Using forms ensures we use cleaned_data instead of raw GET strings.
    """
    title = forms.CharField(max_length=100, required=False, strip=True)

class BookForm(forms.ModelForm):
    """
    Example ModelForm for creating/updating Book - use safe form handling.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # adjust to match your Book model
