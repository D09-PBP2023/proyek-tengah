from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Book(models.Model):
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    original_language = models.CharField(max_length=256)
    year_published = models.IntegerField()
    sales = models.IntegerField()
    genre = models.CharField(max_length=256)
    cover_image = models.ImageField(null=True)

    @property
    def calculate_average_rating(self):
        return Review.objects.filter(book=self).aggregate(avg_rating=Avg('rating'))['avg_rating']

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=512)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)