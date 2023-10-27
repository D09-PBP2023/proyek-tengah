from django.urls import path
from .views import view_profile_byId, view_self_profile, edit_profile


app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:pk>', view_profile_byId, name='view_profile'),
    path('profile/', view_self_profile, name='view_myprofile'),

    
    path('profile/edit/', edit_profile, name='edit_profile'),
]