from django.urls import path
from catalog.views import book_details

app_name = 'catalog'

urlpatterns = [
    path('book_details/<int:id>/', book_details, name='book_details'),
    # path('book/<int:id>/', book, name='book'),
]