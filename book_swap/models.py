from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookSwap(models.Model):
    user = models.CharField(max_length=150)
    acc_user = models.CharField(max_length=150)
    name = models.CharField(max_length=200, default="")
    message = models.TextField(max_length=500)
    swapped = models.BooleanField(default=False)