from django.urls import path

from users.views import login_user, login_user_mobile, logout_user, logout_user_mobile, register_user, register_user_mobile

app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login-mobile/', login_user_mobile, name='login-mobile'),
    path('register-mobile/', register_user_mobile, name='register-mobile'),
    path('logout-mobile/', logout_user_mobile, name='logout-mobile'),
]