import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from main.models import Book
from users.forms import UserRegistrationForm

# Create your views here.
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