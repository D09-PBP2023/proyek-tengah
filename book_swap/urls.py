from django.urls import path
from book_swap.views import request_book_swap, show_json, show_processed_book_swap, show_queue_book_swap
from book_swap.views import show_accepted_book_swap, accept_swap,get_processed_book_json, search_key
from book_swap.views import cancel_swap

app_name = 'book_swap'

urlpatterns = [
    path('waiting_swap/', show_queue_book_swap, name='show_queue_book_swap'), 
    path('book_swap/', show_processed_book_swap, name='show_processed_book_swap'),
    path('accepted_swap/', show_accepted_book_swap, name='show_accepted_book_swap'), 
    path('request_swap/', request_book_swap, name='request_book_swap'),
    path('book_swap/json/', show_json, name='show_json'),
    path('book_swap/search/', search_key, name='search_key'),
    path('accept_swap/<int:id>', accept_swap, name='accept_swap'),
    path('cancel_swap/<int:id>', cancel_swap, name='cancel_swap'),
    path('get_processed_book_json', get_processed_book_json, name='get_processed_book_json'),
]