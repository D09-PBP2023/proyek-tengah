from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from main.models import Book
from user_profile.models import UserProfile
from django.shortcuts import get_object_or_404
from django.core import serializers

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
    return render(request, "book_details.html", context)

def bookmark_book(request, id):
    book = get_object_or_404(Book, pk=id)
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.bookmarkedbooks.filter(id=book.id).exists():
        user_profile.bookmarkedbooks.remove(book)
    else:
        user_profile.bookmarkedbooks.add(book)
    return HttpResponseRedirect(reverse('catalog:book_details', kwargs={"id":id}))


def get_marked_books(request):
    user_profile = UserProfile.objects.get(user=request.user)
    data = user_profile.bookmarkedbooks.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

