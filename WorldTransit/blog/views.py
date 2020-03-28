from django.forms import models
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth import authenticate, login, logout
from .forms import QuestionForm
from django.urls import reverse
import hashlib
from datetime import timezone

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
    return render(request, 'blog/login.html', {'user': user, 'pseudo': pseudo, 'password': password})


def deconnexion(request):
    global user
    # le traitement de deconnection a faire
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
    return render(request, 'blog/useraccount.html', {'user': user})


def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """
    if request.method == 'GET':
        quest = get_object_or_404(Questions, id=2)
        liste = list()
        liste.append(quest)

        resp = Response.objects.filter(user_id=1)
        liste2 = list()
        liste2.append(resp)
        return render(request, 'blog/questionResponse.html', {'quest': liste, 'resp': liste2})

    return render(request, 'blog/questionResponse.html', {'user': user})


def response(request):
    """method for post response"""
    if request.POST.get("reponse") is not None:
        u = Questions(content=request.POST.get("reponse"))
        u.save()
        return render(request, 'blog/questionResponse.html', {'user': user})
    return render(request, 'blog/questionReponse.html', {'user': user})


def questions(request):
    """method for post questions"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            return redirect('useraccount.html')
    else:
        form = QuestionForm()
    return render(request, 'blog/newquestions.html', {'form': form})

    def handler404(request):
        return render(request, 'errors/404.html', status=404)







