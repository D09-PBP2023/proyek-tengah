from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from book_request.forms import RequestBookForm

@csrf_exempt
def request_book_by_ajax(request):
    if request.method == 'POST':
        form = RequestBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an instance of the model without saving it to the database
            user_request = form.save(commit=False)
            user_request.request_status = 'PENDING'
            # Access the data
            name = user_request.name
            author = user_request.author
            original_language = user_request.original_language
            year_published = user_request.year_published
            sales = user_request.sales
            genre = user_request.genre
            cover_image = user_request.cover_image
            # Save the modified instance to the database
            user_request.save()
            return JsonResponse({'error': False, 'message': 'Request Added Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors, 'message': 'Request Failed'})
    else:
        form = RequestBookForm()
        return render(request, 'book_request_by_ajax.html', {'form': form})

def get_book_json(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))