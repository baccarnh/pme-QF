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
    pseudo = request.POST.get("pseudo")
    password = request.POST.get("password")
    global user
    user = pseudo
    return render(request,'blog/login.html',{'user': user,'pseudo': pseudo,'password': password})


def deconnexion(request):
    global user
    #le traitement de deconnection a faire
    user = None
    return render(request, 'home.html', {'user': user})

def signup(request):
    """method for  createaccount """
    #methode a amelioré biesure ici juste pour voir le fonctionement
    if request.POST.get("password") == request.POST.get("confirm_password") and request.POST.get("password") is not None:
        u = Users(name=request.POST.get("name"),
              last_name=request.POST.get("last_name"),
              pseudo=request.POST.get("pseudo"),
              email=request.POST.get("email"),
              job=request.POST.get("job"),
              password=request.POST.get("password")
              )
        u.save()
        return render(request, 'home.html', {'user': user})

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







