from django import forms
from .models import Users, Response, Questions
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'