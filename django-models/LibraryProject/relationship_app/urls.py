from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # your custom views like register

urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Optional: you can still have your previous views for books/libraries
    # path('books/', views.list_books, name='list_books'),
    # path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

