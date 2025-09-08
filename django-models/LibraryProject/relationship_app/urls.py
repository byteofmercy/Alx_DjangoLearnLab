from django.urls import path
from .views import list_books, add_book, edit_book, delete_book

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("books/add_book/", add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", delete_book, name="delete_book"),
]

