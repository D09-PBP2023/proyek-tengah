from django.urls import path
from .views import view_profile_byId, view_self_profile, edit_profile, add_favorite, get_buku_by_id, get_username_by_id


app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:pk>', view_profile_byId, name='view_profile'),
    path('profile/', view_self_profile, name='view_myprofile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('add-favorite/', add_favorite, name='add_favorite'),
    path('get_buku_by_id/<int:id>/', get_buku_by_id, name='get_buku_by_id'),

    path('user/<int:user_id>/', get_username_by_id, name='get_username_by_id'),

]