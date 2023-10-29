from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    original_language = models.CharField(max_length=256)
    year_published = models.IntegerField()
    sales = models.IntegerField()
    genre = models.CharField(max_length=256)
    cover_image = models.ImageField(null=True, upload_to="input/cover")
