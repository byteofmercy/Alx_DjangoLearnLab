from django.contrib import admin
from django.urls import path, include  # make sure include is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # ADD THIS LINE
]
