from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Input


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control',}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control',}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control',}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control',}))
    password1 = forms.CharField( help_text="Your password must contain at least 8 characters." ,widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control',}))
    password2 = forms.CharField(help_text='Enter the same password as before, for verification.',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control mb-2',}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )