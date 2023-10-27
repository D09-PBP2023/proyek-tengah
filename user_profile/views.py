from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from .forms import UserUpdateForm
from users.urls import login_user

def view_self_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': profile})
    else :
        messages.success(request,("Please Log In to view your profile"))
        return redirect('login')


def view_profile_byId(request, pk):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id=pk)
        return render(request, 'profile_byid.html', {'profile': profile})
    else :
        messages.success(request,("Please Log In to view your profile"))
        return HttpResponseRedirect('login/')


#wip
@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = UserUpdateForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})