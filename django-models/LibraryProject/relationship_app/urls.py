from django.urls import path
from .views import (
    admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book
)

urlpatterns = [
    # Role-based URLs
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book permission URLs
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]

