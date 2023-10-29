from django.forms import ModelForm
from book_swap.models import BookSwap
from main.models import Book 
from django import forms

class BookSwapForm(ModelForm):
    name = forms.ModelChoiceField(queryset=Book.objects.all())
    class Meta:
        model = BookSwap
        fields = ["name", "message"]