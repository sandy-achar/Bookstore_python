from django.shortcuts import render, redirect
from .models import Book
from .forms import SearchForm
# Create your views here.

def index_books(request):
    books = Book.objects.all()
    form = SearchForm()
    return render(request, 'book/index.html', {'books':books, 'form':form})

def search_books(request, category, name):
    books = Book.objects.filter(**{category:name})
    form = SearchForm()
    return render(request, 'book/book_search.html', {'books':books, 'form':form})

def search_test(request):
    #POST we need to process data now
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            category = form.cleaned_data['category']
            name = form.cleaned_data['name']

            return redirect('search_books', category=category, name=name)
    else:
        form = SearchForm()

    return render(request, 'book/index.html', {'form':form})
