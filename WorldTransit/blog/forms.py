from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    pseudo = forms.CharField(max_length=255, required=False)
    job = forms.CharField(max_length=255, required=False)
    password = forms.CharField(max_length=255, required=False)

    """class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)"""