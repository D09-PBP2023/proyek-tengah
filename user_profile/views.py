import json
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.http import HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from users.urls import login_user
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from main.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from django.core.serializers import serialize


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


@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile = UserProfile.objects.get(user=request.user)
        user_form = UserForm(request.POST or None, instance=request.user)
        profile_form = UserUpdateForm(request.POST or None, instance=profile)
        context = {'fav1' : profile.favoriteBook1,
                   'fav2' : profile.favoriteBook2,
                   'fav3' : profile.favoriteBook3,
                   'profile': profile,
                   'user':current_user,
                   'userform': user_form,
                   'profileform': profile_form,
                    }

        if request.method == 'POST':
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                login(request, current_user)
                return redirect('user_profile:view_myprofile')

        else:
            user_form = UserForm(instance=request.user)
            profile_form = UserUpdateForm(instance=profile)

        return render(request, 'edit_profile.html', context)
    
    else:
        messages.success(request, ("You Must Be Logged In to Update Your Profile"))
        return redirect('users:login')

#bookmark
@login_required()
def view_bookmarked_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    bookmarked_books = user_profile.bookmarkedbooks.all()
    return render(request, 'bookmarked_list.html', {'bookmarked_books': bookmarked_books})


@csrf_exempt
def add_favorite(request):
    if request.method == "POST":
        formData = request.POST
        favid = formData.get('favId')
        id= formData.get('idBuku')
        book = Book.objects.filter(pk=id)
        user_profile = UserProfile.objects.get(user=request.user)
        if favid == "1":
            user_profile.favoriteBook1 = book[0]
            user_profile.save()
        if favid == "2":
            user_profile.favoriteBook2 = book[0]
            user_profile.save()
        if favid == "3":
            user_profile.favoriteBook3 = book[0]
            user_profile.save()
            
        return HttpResponse(b"Berhasil", status=201)
    return HttpResponseNotFound()

def get_buku_by_id(request, id):
    bukuDicari = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', bukuDicari))


def book_list(request):
    # Get the current logged-in user's profile
    user_profile = UserProfile.objects.get(user=request.user)

    # Get the bookmarked books for the current user
    bmarkedbooks = user_profile.bookmarkedbooks.all()

    # Filter by genre if a genre parameter is passed in the URL
    genre = request.GET.get('genre')
    if genre:
        bmarkedbooks = bmarkedbooks.filter(genre=genre)

    context = {
        'bmarkedbooks': bmarkedbooks,
    }
    return render(request, 'book_list.html', context)

def get_username_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    username = user.username
    
    context = {
        'username': username,
    }
    return render(request, 'username_detail.html', context)

from django.core.serializers import serialize
from django.http import HttpResponse

def get_profile_flutter(request):
    data = UserProfile.objects.get(user=request.user)
    serialized_data = serialize("json", [data])
    return HttpResponse(
        serialized_data,
        content_type="application/json"
    )


@csrf_exempt
def edit_profile_mobile(request):
    if request.method == 'POST':
        formData = request.POST
        profile = UserProfile.objects.get(user=request.user)
        
        profile.nickname = formData.get('nickname')
        profile.email = formData.get('email')
        profile.bio = formData.get('bio')

        profile.save()

        return JsonResponse({"status": True}, status=200)
    else:
        return JsonResponse({"status": False}, status=401)

@csrf_exempt
def edit_fav_mobile(request, favchange):
    if request.method == 'POST':

        formData = request.POST
        profile = UserProfile.objects.get(user=request.user)
        if favchange == 1:
            book_id1 = formData.get('fav1')
            book1 = Book.objects.get(id=book_id1) if book_id1 else None
            profile.favoriteBook1 = book1
        if favchange == 2:
            book_id2 = formData.get('fav2')
            book2 = Book.objects.get(id=book_id2) if book_id2 else None
            profile.favoriteBook2 = book2
            
        if favchange == 3:
            book_id3 = formData.get('fav3')
            book3 = Book.objects.get(id=book_id3) if book_id3 else None
            profile.favoriteBook3 = book3

        profile.save()

        return JsonResponse({"status": True}, status=200)
    else:
        return JsonResponse({"status": False}, status=401)