from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=False, default=None)
    last_name = forms.CharField(max_length=255, default=None)
    pseudo = forms.CharField(max_length=255, default=None)
    job = forms.CharField(max_length=255, default=None)
    password = forms.CharField(max_length=255, default=None)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)