from django.db import models
from main.models import Book
from django.contrib.auth.models import User
from django.db.models.signals import post_save

 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, default=True)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField()
    bookmarkedbooks = models.ManyToManyField(Book, blank=True)
    times_swapped = models.IntegerField(default=0)
    favoriteBook1 = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name='profile_book1', blank=True, null=True)
    favoriteBook2 = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name='profile_book2', blank=True, null=True)
    favoriteBook3 = models.ForeignKey(Book, on_delete=models.SET_NULL, related_name='profile_book3', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


