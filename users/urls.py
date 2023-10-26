from django.urls import path

from users.views import login_user, logout_user, register_user

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]