from django.urls import path
from book_request.views import request_book_by_ajax, get_requested_book_json

app_name = 'book_request'

urlpatterns = [
    path('request-book/', request_book_by_ajax, name='request_book'),
    path('get-requested-book/', get_requested_book_json, name='get_requested_book')
]