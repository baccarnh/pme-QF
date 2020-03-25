from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import SuccessURLAllowedHostsMixin, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from .forms import SignUpForm

def login(request):
    """method for return login.html"""
    return render(request,'blog/login.html')



def signup(request):
    """method for return createaccount.html"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            Users = form.save()
            Users.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            Users.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=Users.username, password=raw_password)
            login(request, Users)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/createaccount.html', {'form': form})




def useraccount(request):
    """method for return useraccount.html"""
    return render(request, 'blog/useraccount.html')

def questionResponse(request):
    """method for return questionResponse.html with some question and response in bdd """
    quest = get_object_or_404(Questions, id=1)
    liste = list()
    liste.append(quest)

    resp = Response.objects.filter(user_id=1)
    liste2 = list()
    liste2.append(resp)
    return render(request, 'blog/questionResponse.html', {'quest':liste, 'resp': liste2})

def handler404(request):
    return render(request,'errors/404.html',status=404)


"""class LoginView(SuccessURLAllowedHostsMixin, FormView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = 'templates/login.html'"""


"""def login(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})"""


"""def createaccount(request):
    if request.method == 'POST':
        form = Users(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Users()
    return render(request, 'blog/createaccount.html', {'form': form})"""


"""def signout(request):
    logout(request)
    return redirect('login')"""
