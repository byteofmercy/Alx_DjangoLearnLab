# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home')  # Redirect to home page (we will define it in urls)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (using Django's built-in)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (using Django's built-in)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
