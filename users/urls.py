from django.urls import path

from users.views import login_user, register_user

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]