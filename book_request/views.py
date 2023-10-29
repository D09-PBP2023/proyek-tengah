from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Book, RequestBook
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from book_request.forms import RequestBookForm

@csrf_exempt
def request_book_by_ajax(request):
    if request.method == 'POST':
        form = RequestBookForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an instance of the model without saving it to the database
            user_request = form.save(commit=False)
            user_request.request_status = 'PENDING'
            user_request.user = request.user
            # Save the modified instance to the database
            user_request.save()
            return JsonResponse({'error': False, 'message': 'Request Added Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors, 'message': 'Request Failed'})
    else:
        form = RequestBookForm()
        return render(request, 'book_request_by_ajax.html', {'form': form})

@login_required
def get_requested_book_json(request):
    data = RequestBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")