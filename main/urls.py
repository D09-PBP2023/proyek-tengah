from django.urls import path
from main.views import get_books, get_books_by_genre, get_books_by_name, show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get-books/', get_books, name='get_books'),
    path('get-books-by-name/<str:name>', get_books_by_name, name='get_books_by_name'),
    path('get-books-by-genre/<str:name>', get_books_by_genre, name='get_books_by_genre'),
]