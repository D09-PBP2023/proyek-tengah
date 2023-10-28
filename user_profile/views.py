from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.models import User
from users.urls import login_user
from django.contrib.auth import authenticate, login, logout

def view_self_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        context = {'fav1' : profile.favoriteBook1,
                   'fav2' : profile.favoriteBook2,
                   'fav3' : profile.favoriteBook3,
                   'profile': profile,
                   }
        return render(request, 'profile.html', context)
    else :
        messages.success(request,("Please Log In to view your profile"))
        return redirect('users:login')


def view_profile_byId(request, pk):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id=pk)
        return render(request, 'profile_byid.html', {'profile': profile})
    else :
        messages.success(request,("Please Log In to view your profile"))
        return redirect('users:login')


#wip
@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.get(user=request.user)
        form = UserUpdateForm(request.POST or None, instance=profile)
        context = {'fav1' : profile.favoriteBook1,
                   'fav2' : profile.favoriteBook2,
                   'fav3' : profile.favoriteBook3,
                   'profile': profile,
                   'user':current_user,
                   'form': form,
                    }

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                login(request, current_user)
                return redirect('user_profile:view_myprofile')

        else:
            form = UserUpdateForm(instance=profile)

        return render(request, 'edit_profile.html', context)
    
    else:
        messages.success(request, ("You Must Be Logged In to Update Your Profile"))
        return redirect('users:login')

#bookmark
def view_bookmarked_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    bookmarked_books = user_profile.bookmarkedbooks.all()
    return render(request, 'bookmarked_list.html', {'bookmarked_books': bookmarked_books})
