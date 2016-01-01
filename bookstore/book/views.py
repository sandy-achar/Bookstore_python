from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Book
from .forms import SearchForm, UserForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

def index_books(request, currentUser=None):
    books = Book.objects.all()
    form = SearchForm()
    user = UserForm()
    register = RegisterForm()
    return render(request, 'book/index.html', {'books':books, 'form':form, 'userLogin':user, 'register':register, 'currentUser':currentUser})

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

            return redirect('search_book', category=category, name=name)

    return redirect('index_books')

def register_user(request):
    # if its a POST we need to process the data
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Save the user into the database
            user = User.objects.create_user(username=username, email=email, password=password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

    return redirect('index_books')

def login_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(user)
                print("Authentication successful!")
            return redirect('index_books', user)

        else:
            print("Invalid form")
            return redirect('index_books')

    else:
        return redirect('index_books')
