from django.forms import ModelForm
from main.models import Book

class RequestBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "original_language", "year_published", "sales", "genre", "cover_image"]