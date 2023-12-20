from django.urls import path
from book_swap.views import show_json, show_processed_book_swap, show_queue_book_swap
from book_swap.views import show_accepted_book_swap, accept_swap,get_processed_book_json, search_key
from book_swap.views import cancel_swap
from book_swap.views import create_swap_mobile, create_swap, show_create_swap
from book_swap.views import get_model_data, delete_all_swap
from book_swap.views import get_processed_book_json, get_waiting_accept_book_json, get_accepted_book_json, get_finished_book_json
from book_swap.views import cancel_swap_mobile, accept_swap_mobile, finish_swap_mobile
app_name = 'book_swap'

urlpatterns = [
    path('delete_all_swap/', delete_all_swap, name='delete_all_swap'),
    path('get_model_data/', get_model_data, name='get_model_data'),
    path('create_swap/', create_swap, name='create_swap'),
    path('create_swap_page/', show_create_swap, name='show_create_swap'),
    path('waiting_swap/', show_queue_book_swap, name='show_queue_book_swap'), 
    path('book_swap/', show_processed_book_swap, name='show_processed_book_swap'),
    path('accepted_swap/', show_accepted_book_swap, name='show_accepted_book_swap'), 
    path('book_swap/json/', show_json, name='show_json'),
    path('book_swap/search/', search_key, name='search_key'),
    path('accept_swap/', accept_swap, name='accept_swap'),
    path('cancel_swap/', cancel_swap, name='cancel_swap'),
    path('get_processed_book_json/', get_processed_book_json, name='get_processed_book_json'),
    path('get_waiting_accept_book_json/', get_waiting_accept_book_json, name='get_waiting_accept_book_json'),
    path('get_accepted_book_json/', get_accepted_book_json, name='get_accepted_book_json'),
    path('get_finished_book_json/', get_finished_book_json, name='get_finished_book_json'),
    path('create_swap_mobile/', create_swap_mobile, name='create_swap_mobile'),
    path('cancel_swap_mobile/', cancel_swap_mobile, name='cancel_swap_mobile'),
    path('accept_swap_mobile/', accept_swap_mobile, name='accept_swap_mobile'),
    path('finish_swap_mobile/', finish_swap_mobile, name='finish_swap_mobile'),
]