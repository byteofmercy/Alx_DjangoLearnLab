from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Project 1 URLs
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Project 2 URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]



