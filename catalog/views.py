from django.shortcuts import render
from main.models import Book

# Create your views here.

def book_details(request, id):
    book = Book.objects.get(pk = id)

    context = {
        'name': book.name,
        'author': book.author,
        'original_language': book.original_language,
        'year_published': book.year_published,
        'sales' : book.sales,
        'genre' : book.genre,
        'cover_image' : book.cover_image
    }
    return render(request, "book_details.html", context)

# def book(request, id):
#     book = Book.objects.get(pk = id)

#     context = {
#         'name': book.name,
#         'author': book.author,
#         'original_language': book.original_language,
#         'year_published': book.year_published,
#         'sales' : book.sales,
#         'genre' : book.genre,
#         'cover_image' : book.cover_image
#     }
#     return render(request, "book.html", context)