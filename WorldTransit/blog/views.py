from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import hashlib

"""variable global"""
user = None


def home(request):

    return render(request, 'home.html', {'user': user})


def connexion(request):
    """method for connexion"""
    global user
    user = 'nicos'
    return render(request,'blog/login.html',{'user': user})


def deconnexion(request):
    global user
    #le traitement de deconnection a faire
    user = None
    return render(request, 'home.html', {'user': user})

def signup(request):
    """method for return createaccount.html"""

    return render(request, 'blog/createaccount.html', {'user': user})


def useraccount(request):
    """method for return useraccount.html"""
    return render(request, 'blog/useraccount.html', {'user': user})


def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """

    return render(request, 'blog/questionResponse.html', {'user': user})


def response(request):
    """method for post response"""

    return render(request, 'blog/questionReponse.html', {'user': user})
    

def questions(request):
    """method for post questions"""

    return render(request, 'blog/newquestions.html', {'user': user})







