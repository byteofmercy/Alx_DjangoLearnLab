from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple home view for redirect after registration
def home(request):
    return HttpResponse("Welcome to the Home Page!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('', include('relationship_app.urls')),  # Authentication URLs
]
