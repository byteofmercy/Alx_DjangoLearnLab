from django.urls import path
from .views import BookListView, LibraryDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]

