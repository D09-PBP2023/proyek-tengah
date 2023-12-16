from django.urls import path
from main.views import get_books, get_books_by_name, show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_books/', get_books, name='get_books'),
    path('get_books_by_name/<str:name>', get_books_by_name, name='get_books_by_name'),
]