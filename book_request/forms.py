from django.forms import ModelForm
from .models import RequestBook

class RequestBookForm(ModelForm):
    class Meta:
        model = RequestBook
        fields = ["name", "author", "original_language", "year_published", "sales", "genre", "cover_image"]