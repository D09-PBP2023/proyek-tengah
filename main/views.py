from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from main.models import Book

# Create your views here.
def show_main(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "main.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )