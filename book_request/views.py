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
            form.save()
            return JsonResponse({'error': False, 'message': 'Request Added Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors, 'message': 'Request Failed'})
    else:
        form = RequestBookForm()
        return render(request, 'book_request_by_ajax.html', {'form': form})

def get_book_json(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))