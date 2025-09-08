from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .models import Book, UserProfile

# -----------------------------
# Role-based view helpers
# -----------------------------
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# -----------------------------
# Role-based views
# -----------------------------
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")

# -----------------------------
# Book views
# -----------------------------
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

@login_required
@permission_required('relationship_app.add_book', raise_exception=True)
def add_book_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author)
        return redirect("list_books")
    return render(request, "add_book.html")

@login_required
@permission_required('relationship_app.change_book', raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("list_books")
    return render(request, "edit_book.html", {"book": book})

@login_required
@permission_required('relationship_app.delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "delete_book.html", {"book": book})

