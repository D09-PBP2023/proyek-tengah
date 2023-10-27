from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from main.models import Book
from user_profile.models import UserProfile
from django.shortcuts import get_object_or_404

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
        'cover_image' : book.cover_image,
        'id' : book.pk
    }
    print("hai?")
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


# def bookmark_book(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
    
#     user_profile = UserProfile.objects.get(user=request.user)
#     if user_profile.bookmarkedbooks.get(book).exists():
#         user_profile.bookmarkedbooks.remove(book)
#     else:
#         user_profile.bookmarkedbooks.remove(book)
#     return HttpResponseRedirect(reverse('catalog:book_details/book_id')) 

def bookmark_book(request, id):
    print("HAAALOOO")
    book = get_object_or_404(Book, pk=id)
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.bookmarkedbooks.filter(id=book.id).exists():
        user_profile.bookmarkedbooks.remove(book)
        print("removed")
    else:
        user_profile.bookmarkedbooks.add(book)
        print("masuk")
    return HttpResponseRedirect(reverse('catalog:book_details', kwargs={"id":id}))
