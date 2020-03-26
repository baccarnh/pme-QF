from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import SuccessURLAllowedHostsMixin, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from .forms import SignUpForm, ResponseForm, QuestionForm

def login(request):
    """method for return login.html"""
    return render(request,'blog/login.html')



def signup(request):
    """method for return createaccount.html"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            return redirect('blog/useraccount.html')
    else:
        form = SignUpForm()
    return render(request, 'blog/createaccount.html', {'form': form})


def useraccount(request):
    """method for return useraccount.html"""
    quest = Questions.objects.filter(author='nicos', status=None)
    liste = list()
    liste.append(quest)
    return render(request, 'blog/useraccount.html', {'quest': liste})



def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """
    if request.method == 'GET':
        quest = get_object_or_404(Questions, id=1)
        liste = list()
        liste.append(quest)

        resp = Response.objects.filter(user_id=1)
        liste2 = list()
        liste2.append(resp)
        return render(request, 'blog/questionResponse.html', {'quest':liste, 'resp': liste2})



def response(request):
    """method for post response"""
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            return redirect('blog/questionResponse.html')
    else:
        form = ResponseForm()
    return render(request, 'blog/useraccount.html', {'form': form})
    


def questions(request):
    """method for post questions"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            return redirect('blog/useraccount.html')
    else:
        form = QuestionForm()
    return render(request, 'blog/createaccount.html', {'form': form})


def handler404(request):
    return render(request,'errors/404.html',status=404)


