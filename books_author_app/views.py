from django.shortcuts import render, redirect
from books_author_app.models import *

# Create your views here.

# Display views
def index(request):
    context={
        'books':Book.objects.all()
    }
    return render(request, 'index.html', context)

def book_info(request,id):
    context={
        'book': Book.objects.get(id=id),
        'authors': Author.objects.all(),
    }
    return render(request, 'bookinfo.html', context)

def author_info(request,id):
    context={
        'author': Author.objects.get(id=id),
        'books': Book.objects.all(),
    }
    return render(request, 'authorinfo.html', context)

def authors(request):
    context={
        'authors': Author.objects.all(),
    }
    return render(request, 'authors.html', context) 





# Action views
def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['description'],
    )
    return redirect('/')

def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'],
    )
    return redirect('/authors')

def author_to_book(request,book_id):
    author_to_add = Author.objects.get(id=request.POST["new_author"])
    book_added = Book.objects.get(id=book_id)
    book_added.authors.add(author_to_add)
    return redirect(f'/books/{book_added.id}')

def book_to_author(request,author_id):
    book_to_add = Book.objects.get(id=request.POST["new_book"])
    author_added = Author.objects.get(id=author_id)
    author_added.books.add(book_to_add)
    return redirect(f'/authors/{author_added.id}')
