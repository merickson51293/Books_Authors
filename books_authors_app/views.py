from django.shortcuts import render, redirect
from books_authors_app.models import *

def home(request):
    return render(request, "home.html")

def book(request):
    context = {
        "all_books": Book.objects.all(),
    }
    return render(request, "book.html", context)

def author(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "author.html", context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc'],
    )
    return redirect('/book')

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'],
        book_id=request.POST['books']
    )
    return redirect('/author')

def book_desc(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books__id=book_id)
    }
    return render(request, "book_desc.html", context)

def author_desc(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id=author_id)
    }
    return render(request, "author_desc.html", context)

def assign_author(request, author_id):
    book = Book.objects.get(id=request.POST['book_id'])
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f"/author_desc.html/{author_id}")

def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f"/book_desc.html/{book_id}")