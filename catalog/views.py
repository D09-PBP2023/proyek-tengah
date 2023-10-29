from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from main.models import Book, Review
from user_profile.models import UserProfile
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

@login_required()
def bookmark_book(request, id):
    book = get_object_or_404(Book, pk=id)
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.bookmarkedbooks.filter(id=book.id).exists():
        user_profile.bookmarkedbooks.remove(book)
    else:
        user_profile.bookmarkedbooks.add(book)
    return HttpResponseRedirect(reverse('catalog:book_details', kwargs={"id":id}))

@login_required()
def get_marked_books(request):
    user_profile = UserProfile.objects.get(user=request.user)
    data = user_profile.bookmarkedbooks.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def get_review(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)
    
    data = []

    for review in reviews:
        data.append({
            "id": review.pk,
            "book": book.pk,
            "user": review.user.username,
            "review": review.review,
            "rating": review.rating,
            "created_at": review.created_at
        })

    return JsonResponse(data, safe=False)

@csrf_exempt
def add_review(request, id):
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        book = get_object_or_404(Book, pk=id)
        user = request.user
        
        new_review = Review(book=book, user=user, rating=rating, review=review)
        new_review.save()
        
        return HttpResponse(b"CREATED", status=201)
        
    return HttpResponseNotFound()


def get_average_rating(request, id):
    book = get_object_or_404(Book, pk=id)
    average_rating = book.calculate_average_rating()
    return JsonResponse({'average_rating': average_rating})