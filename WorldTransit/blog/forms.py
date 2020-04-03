from django.db import models
from django import forms
from django.forms import ModelForm
from .models import Users, Questions, Response

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = '__all__'
