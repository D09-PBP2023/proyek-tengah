from django.forms import ModelForm
from book_swap.models import BookSwap
from main.models import Book
from django import forms    

class BookSwapForm(ModelForm):
    bookslib = Book.objects.all()
    book_choose_list = []
    count = 0
    for book in bookslib:
        book_choose_list.append((book.name, book.name))
        book_choose = tuple(book_choose_list)

    name = forms.CharField(widget=forms.Select(choices=book_choose))    
    class Meta:
        model = BookSwap
        fields = ["name", "message"]