from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-full h-full px-2 py-1', 'placeholder': 'Username'}), max_length=64)
    # first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    # last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    # email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-full h-full px-2 py-1', 'placeholder': 'Password'}), max_length=64)
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-full h-full px-2 py-1', 'placeholder': 'Password Again'}), max_length=64)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields # + ('first_name', 'last_name', 'email',)