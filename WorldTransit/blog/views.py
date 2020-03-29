from django.forms import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth import authenticate, login, logout
from .forms import QuestionForm, ResponseForm
from django.urls import reverse
import hashlib
from datetime import timezone

"""variable global"""
user = None


def home(request):
    return render(request, 'home.html', {'user': user})


def connexion(request):
    """method for connexion"""
    global user
    if user is None:
        pseudo = request.POST.get("pseudo")
        password = request.POST.get("password")
        user = pseudo
        return render(request, 'blog/login.html', {'user': user, 'pseudo': pseudo, 'password': password})
    else:
        return render(request, 'home.html', {'user': user})


def deconnexion(request):
    # le traitement de deconnection a faire
    global user
    logout(request)
    user = None
    return render(request, 'home.html', {'user': user})


def signup(request):
    """method for  createaccount """
    # create new user account
    if request.POST.get("password") == request.POST.get("confirm_password") and request.POST.get(
            "password") is not None:
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
    quest = Questions.objects.filter( user_id= 1)
    liste = list()
    liste.append(quest)
    return render(request, 'blog/useraccount.html', {'user': user, 'quest': liste})


def response(request):
    """method for display question and response """
    global user
    # i get the objezct in bdd and i add it in list
    quest = get_object_or_404(Questions, id=2)
    liste = list()
    liste.append(quest)
    # i get the objezct in bdd and i add it in list
    resp = Response.objects.filter(user_id=1)
    liste2 = list()
    liste2.append(resp)
    """i display form with django forms based in class response in models 
        with class meta in forms.py"""
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        #if the form is ok
        if form.is_valid():
            resp = form.save()
            resp.refresh_from_db()  # load the profile instance created by the signal
            resp.save()
            #i save it and i return to home page
            return redirect('home')
    else:# else a resent the pages with form
        form = ResponseForm()
        #i show the pages and i send the list and the form for dsiplay elems
    return render(request, 'blog/questionResponse.html', {'quest': liste, 'resp': liste2, 'form': form})


def questions(request):
    """i display form with django forms based in class response in models
           with class meta in forms.py"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        #if the form is ok
        if form.is_valid():
            quest = form.save()
            quest.refresh_from_db()  # load the profile instance created by the signal
            quest.save()
            #i save it in the bdd
            #and return to usercaccount page
            return redirect('useraccount.html')
    else:
        form = QuestionForm()
        #if the form is not ok  display again the page and send form to display this in html
    return render(request, 'blog/newquestions.html', {'form': form})

    def handler404(request):
        return render(request, 'errors/404.html', status=404)







