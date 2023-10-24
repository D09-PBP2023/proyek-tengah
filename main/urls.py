from django.urls import path
from main.views import get_books, show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_books/', get_books, name='get_books')
]