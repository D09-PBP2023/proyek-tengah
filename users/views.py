import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from main.models import Book
from users.forms import UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main:show_main"))
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("main:show_main"))
    
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('users:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    return redirect('users:login')

# Mobile
@csrf_exempt
def login_user_mobile(request):
    if request.user.is_authenticated:
        print(request.user)
        return JsonResponse({
            "status": False,
            "message": "You have signed in."
        }, status=400)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
                "status": True,
                "message": "Sorry, incorrect username or password. Please try again."
            }, status=401)
    return JsonResponse({
        "status": False,
        "message": "Method not allowed."
    }, status=405)

@csrf_exempt
def register_user_mobile(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "You have signed in."
        }, status=400)
    
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "Successfully Signed Up!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Sorry, invalid username or password. Please try again."
            }, status=400)
    
    return JsonResponse({
        "status": False,
        "message": "Method not allowed."
    }, status=405)

@csrf_exempt
def logout_user_mobile(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "You have not signed in."
        }, status=400)

    logout(request)
    return JsonResponse({
        "status": True,
        "message": "Successfully Logged Out!"
    }, status=200)
