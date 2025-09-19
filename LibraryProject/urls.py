from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # only if you have bookshelf/urls.py
]
