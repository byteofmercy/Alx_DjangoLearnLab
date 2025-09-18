# LibraryProject/LibraryProject/urls.py (snippet)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),   # root points to bookshelf app
]
