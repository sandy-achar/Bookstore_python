from django.shortcuts import render
from .models import Book
from random import sample

# Create your views here.

def index_books(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {'books':books})

def search_books(request, category, name):
    books = Book.objects.filter(**{category:name})
    return render(request, 'book/book_search.html', {'books':books})
