from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookshelf.urls')),  # <-- add this
]
