from datetime import datetime

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
    liste = Users.objects.all()
    for u in liste:
        if u.email == request.POST.get("email") and u.password == hashlib.sha1(request.POST.get("password").encode()).hexdigest():
            global user
            user = u
            return render(request,'home.html',{'user':user})
    return render(request,'blog/login.html',{'user': user})


def deconnexion(request):
    global user
    user = None
    return render(request, 'home.html', {'user': user})

def signup(request):
    """method for  createaccount """
    liste = Users.objects.all()
    for el in liste:
        if el.email == request.POST.get("email"):
            return render(request, 'blog/createaccount.html', {'user': user,'message':'e-maill existe déja'})

    if request.POST.get("password") == request.POST.get("confirm_password") and request.POST.get("password") is not None:
        password = request.POST.get("password").encode()
        password = hashlib.sha1(password).hexdigest()
        u = Users(name=request.POST.get("name"),
              last_name=request.POST.get("last_name"),
              pseudo=request.POST.get("pseudo"),
              email=request.POST.get("email"),
              job=request.POST.get("job"),
              password=password
              )
        u.save()
        return render(request, 'home.html', {'user': user,'liste':liste})
    return render(request, 'blog/createaccount.html', {'user': user})


def useraccount(request):
    """method for return useraccount.html"""
    return render(request, 'blog/useraccount.html', {'user': user})


def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """
    liste_question = Questions.objects.all()
    liste_response = Response.objects.all()
    return render(request, 'blog/questionResponse.html', {'user': user,'liste_question':liste_question,
                                                          'liste_response':liste_response})


def response(request):
    """method for post response"""

    return render(request, 'blog/questionReponse.html', {'user': user})
    

def questions(request):
    """method for post questions"""
    if user is not None and request.POST.get("title") is not None:
        q = Questions(
                  title=request.POST.get("title"),
                  content=request.POST.get("message"),
                  publishing_date= datetime.now(),
                  user = user
                  )
        q.save()

    return render(request, 'blog/newquestions.html', {'user': user})







