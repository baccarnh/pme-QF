from datetime import datetime
from django.shortcuts import render
from .models import Questions, Response, Users
from .forms import UsersForm, ResponseForm, QuestionsForm
import hashlib

"""variable global"""
user = None

def home(request):
    return render(request, 'home.html', {'user': user})

def connexion(request):
    """method for connexion"""
    liste = Users.objects.all()
    for u in liste:
        if u.email == request.POST.get("email") and u.password == request.POST.get("password"):
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
    form = UsersForm()
    if request.POST == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html', {'user': user,'liste':liste})
    return render(request, 'blog/createaccount.html', {'user': user, 'form': form})


def useraccount(request):
    """method for return response.html"""
    return render(request, 'blog/response.html', {'user': user})


def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """
    liste_question = Questions.objects.all()
    liste_response = Response.objects.all()
    return render(request, 'blog/questionResponse.html', {'user': user,'liste_question':liste_question,
                                                          'liste_response':liste_response})

def questions(request):
    """method for post new questions"""
    liste = Questions.objects.all()
    form = QuestionsForm()
    if request.POST == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'home.html', {'user': user,'liste':liste})
    form = QuestionsForm()
    return render(request, 'blog/newquestions.html', {'user': user, 'form': form})


def response(request,question_id):
    liste = Questions.objects.all()
    if request.POST == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'user': user, 'liste': liste})
    return render(request, 'blog/response.html', {'user': user})






