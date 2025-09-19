
# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.create_book, name='create_book'),
    path('raw/', views.example_raw_query_parametrized, name='raw_query'),
]
