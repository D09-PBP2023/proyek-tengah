from django.urls import path
from catalog.views import book_details, bookmark_book
from user_profile.views import view_bookmarked_list

app_name = 'catalog'

urlpatterns = [
    path('book_details/<int:id>/', book_details, name='book_details'),
    # path('book/<int:id>/', book, name='book'),
    path('bookmark_book/<int:id>/', bookmark_book, name='bookmark_book'),
    path('bookmarked/', view_bookmarked_list, name='view_bookmarked_list'),
]