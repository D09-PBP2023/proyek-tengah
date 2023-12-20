from django.urls import path
from book_request.views import request_book_by_ajax, get_requested_book_json, view_all_requests, approve_request, reject_request, request_book_mobile

app_name = 'book_request'

urlpatterns = [
    path('request-book/', request_book_by_ajax, name='request_book'),
    path('get-requested-book/', get_requested_book_json, name='get_requested_book'),
    path('requests/', view_all_requests, name='view_all_requests'),
    path('requests/approve/<int:request_id>', approve_request, name='approve_request'),
    path('requests/reject/<int:request_id>', reject_request, name='reject_request'),
    path('request-book-mobile/', request_book_by_ajax, name='request_book_mobile'),
]