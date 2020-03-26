from django import forms
from .models import Users, Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

"""class SignUpForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255, required=False)
    pseudo = forms.CharField(max_length=255, required=False)
    job = forms.CharField(max_length=255, required=False)
    password = forms.CharField(max_length=255, required=False)"""

    #class Meta:
       # model = User


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
    """title = forms.CharField(label='title', max_length=255, required=False)
    content = forms.CharField(label='reponse', required=False)
    publishing_date = forms.DateTimeField(label='date',required=False)
    updated_date = forms.DateTimeField(label='update',required=False)
    author = forms.CharField(label='auteur', max_length=255, required=False)
    #user = forms.ForeignKey(Users, on_delete=forms.CASCADE, required=False)"""

