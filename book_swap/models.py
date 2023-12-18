from django.db import models
from django.contrib.auth.models import User
from main.models import Book
# Create your models here.
class BookSwap(models.Model):
    from_user = models.CharField(max_length=100, default='')
    to_user = models.CharField(max_length=100, default='') 
    have_book = models.TextField(max_length=500, default='')
    want_book = models.TextField(max_length=500)
    from_message = models.TextField(max_length=500)
    to_message = models.TextField(max_length=500, default='')
    processed = models.BooleanField(default=False)
    swapped = models.BooleanField(default=False)