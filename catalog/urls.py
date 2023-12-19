from django.urls import path
from catalog.views import book_details, bookmark_book, bookmark_book_flutter, get_marked_books, get_review, add_review, get_average_rating, create_review_flutter
from user_profile.views import view_bookmarked_list

app_name = 'catalog'

urlpatterns = [
    path('book_details/<int:id>/', book_details, name='book_details'),
    # path('book/<int:id>/', book, name='book'),
    path('bookmark_book/<int:id>/', bookmark_book, name='bookmark_book'),
    path('bookmarked/', view_bookmarked_list, name='view_bookmarked_list'),
    path('get_marked_books/', get_marked_books, name='get_marked_books'),
    path('get_review/<int:id>/', get_review, name='get_review'),
    path('add_review/<int:id>/', add_review, name='add_review'),
    path('get_average_rating/<int:id>/', get_average_rating, name='get_average_rating'),
    path('add-review-flutter/', create_review_flutter, name='create_review_flutter'),
    path('bookmarkflutter/<int:id>/', bookmark_book_flutter, name='bookmark_book_flutter'),
]
