from django.forms import ModelForm
from book_swap.models import BookSwap

class BookSwapForm(ModelForm):
    class Meta:
        model = BookSwap
        fields = ["name", "message"]