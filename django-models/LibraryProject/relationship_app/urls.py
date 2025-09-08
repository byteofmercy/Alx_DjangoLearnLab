from django.urls import path
from .views import (
    list_books,
    add_book_view,
    edit_book_view,
    delete_book_view,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("add_book/", add_book_view, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book_view, name="edit_book"),
    path("delete_book/<int:book_id>/", delete_book_view, name="delete_book"),
    path("admin/", admin_view, name="admin_view"),
    path("librarian/", librarian_view, name="librarian_view"),
    path("member/", member_view, name="member_view"),
]
