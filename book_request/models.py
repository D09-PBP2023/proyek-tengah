from django.db import models
from django.conf import settings
from main.models import Book

class RequestBook(models.Model):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]
    
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    original_language = models.CharField(max_length=256)
    year_published = models.IntegerField()
    sales = models.IntegerField()
    genre = models.CharField(max_length=256)
    cover_image = models.ImageField(null=True, upload_to="input/cover")
    request_date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=PENDING)