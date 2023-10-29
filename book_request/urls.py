from django.urls import path
from book_request.views import request_book_by_ajax, get_book_json

app_name = 'book_request'

urlpatterns = [
    path('request-book/', request_book_by_ajax, name='request_book_by_ajax'),
    path('get-book/', get_book_json, name='get_book_json'),
]