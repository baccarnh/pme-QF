from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import SignUpForm, ResponseForm, QuestionForm, ConnexionForm

def connexion(request):
    """method for return login.html"""
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            user = authenticate(username=name, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()
    return render(request,'blog/useraccount.html', locals())

def deconnexion(request):
    """method for log out user account"""
    logout(request)
    return redirect(reverse(connexion))

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

@login_required
def useraccount(request):
    """method for return useraccount.html"""
    quest = Questions.objects.filter(author='nicos', status=None)
    liste = list()
    liste.append(quest)
    return render(request, 'blog/useraccount.html', {'quest': liste})


@login_required
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


@login_required
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
    return render(request, 'blog/questionReponse.html', {'form': form})
    

@login_required
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
    return render(request, 'blog/newquestions.html', {'form': form})


def handler404(request):
    return render(request,'errors/404.html',status=404)


