from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q

from main.models import Book

# Create your views here.
def show_main(request):
    context = {
        'books': Book.objects.all(),
        'user': request.user,
        'n': range(5) # TODO: WILL BE REMOVED BEFORE PRODUCTION
    }
    return render(request, "main.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def get_books_by_name(request, name):
    data = Book.objects.filter(Q(name__icontains=name) | Q(author__icontains=name))
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def get_books_by_id(request):
    id_list = [int(x) for x in request.GET.get('id').split(',')]
    data = Book.objects.filter(pk__in=id_list)
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )