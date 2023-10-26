from django.urls import path, re_path, register_converter
from main.views import get_books, get_books_by_id, get_books_by_name, show_main

app_name = 'main'

# TODO: WILL BE REMOVED IF NOT IMPORTANT ANYMORE BEFORE PRODUCTION
class ListOfIntegerConverter:
    regex = r'\b(\d+)\b'

    def to_python(self, value):
        print(value)
        return [int(x) for x in value.split(',')]

    def to_url(self, value):
        print(value)
        return ','.join(value)

register_converter(ListOfIntegerConverter, "lin")

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_books/', get_books, name='get_books'),
    path('get_books_by_name/<str:name>', get_books_by_name, name='get_books_by_name'),
    path('get_books_by_id/', get_books_by_id, name='get_books_by_id'),
]