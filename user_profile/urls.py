from django.urls import path
from .views import *


app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:pk>', view_profile_byId, name='view_profile'),
    path('profile/', view_self_profile, name='view_myprofile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('add-favorite/', add_favorite, name='add_favorite'),
    path('get_buku_by_id/<int:id>/', get_buku_by_id, name='get_buku_by_id'),

    path('user/<int:user_id>/', get_username_by_id, name='get_username_by_id'),
    path('profileflutter/', get_profile_flutter, name='view_flutter'),
    path('editprofile-mobile/', edit_profile_mobile, name='edit_profile_flutter'),
    path('fav-mobile/<int:favchange>', edit_fav_mobile, name='fav-mobile'),

    

]