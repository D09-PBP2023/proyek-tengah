from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.core import serializers
from .models import Book, RequestBook
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from book_request.forms import RequestBookForm
from main.models import Book
import json

@csrf_exempt
def request_book_by_ajax(request):
    if request.method == 'POST':
        form = RequestBookForm(request.POST, request.FILES)
        if form.is_valid():
            user_request = form.save(commit=False)
            user_request.request_status = 'PENDING'
            user_request.user = request.user
            user_request.save()
            return JsonResponse({'status': True, 'message': 'Request Added Successfully'})
        else:
            return JsonResponse({'status': False, 'errors': form.errors, 'message': 'Request Failed'})
    else:
        form = RequestBookForm()
        return render(request, 'book_request_by_ajax.html', {'form': form})

# @csrf_exempt
# def request_book_by_ajax(request):
#     if request.method == 'POST':
#         name = request.POST.get("name")
#         author = request.POST.get("author")
#         original_language = request.POST.get("original_language")
#         year_published = request.POST.get("year_published")
#         sales = request.POST.get("sales")
#         genre = request.POST.get("genre")
#         cover_image = request.POST.get("cover_image")
#         user = request.user
#         request_status = "PENDING"
#         new_book_request = RequestBook(name=name, author=author, original_language=original_language,
#         year_published=year_published, sales=sales, genre=genre, cover_image=cover_image, user=user, request_status=request_status)
#         new_book_request.save()
#         return HttpResponse(b"CREATED REQUEST", status=201)
#     return HttpResponseNotFound()

@csrf_exempt
def request_book_mobile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_book_request = RequestBook.objects.create(
            user = request.user,
            name = data['name'],
            author = data['author'],
            original_language = data['original_language'],
            year_published = int(data['year_published']),
            sales = int(data['sales']),
            genre = data['genre'],
            cover_image = data['cover_image']
        )
        new_book_request.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@login_required
def get_requested_book_json(request):
    data = RequestBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@staff_member_required
def view_all_requests(request):
    all_requests = RequestBook.objects.all()
    return render(request, 'all_book_requests.html', {'requests': all_requests})

@csrf_exempt
def approve_request(request, request_id):

    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to perform this action.")
    
    req = get_object_or_404(RequestBook, pk=request_id)
    req.request_status = RequestBook.APPROVED
    req.save()

    if request.method == 'POST':
        data = json.loads(request.body)
        
        new_book = Book.objects.create(
            name = data["name"],
            author = data["author"],
            original_language = data["original_language"],
            year_published = data["year_published"],
            sales = data["sales"],
            genre = data["genre"],
            cover_image = data["cover_image"]
        )
        new_book.save()

        return JsonResponse({"status": "success"}, status = 200)
    else:
        return JsonResponse({"status": "failed"}, status = 401)

def load_books():
    with open('main:fixtures/initial_books.json', 'r') as file:
        return json.load(file)
        
@csrf_exempt
def reject_request(request, request_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to perform this action.")
    
    req = get_object_or_404(RequestBook, pk=request_id)
    req.request_status = RequestBook.REJECTED
    req.save()
    return redirect('view_all_requests') 