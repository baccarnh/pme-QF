from django.shortcuts import render, redirect
from blog.models import Questions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import SuccessURLAllowedHostsMixin, FormView


def home(request):

    return render(request, 'home.html')








