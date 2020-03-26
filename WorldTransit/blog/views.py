from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response, Users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import SuccessURLAllowedHostsMixin, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from .forms import SignUpForm, ResponseForm

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
            """name = form.cleaned_data.get('name')
            last_name = form.cleaned_data.get('last_name')
            pseudo = form.cleaned_data.get('pseudo')
            job = form.cleaned_data.get('job')
            password = form.cleaned_data.get('password')"""
            #login(request, Users)
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

#def newquesttion():

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
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            """name = form.cleaned_data.get('name')
            last_name = form.cleaned_data.get('last_name')
            pseudo = form.cleaned_data.get('pseudo')
            job = form.cleaned_data.get('job')
            password = form.cleaned_data.get('password')"""
            #login(request, Users)
            return redirect('blog/questionResponse.html')
    else:
        form = ResponseForm()
    return render(request, 'blog/useraccount.html', {'form': form})
    
    """"# if this is a POST request we need to process the form data

        # create a form instance and populate it with data from the request:
    form = response(request.Post or None)
        # check whether it's valid:
    if form.is_valid():
        Response = form.save()
        Response.refresh_from_db()
        Response.save()
        title =  form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        publishing_date = form.cleaned_data.get('date')
        updated_date = form.cleaned_data.get('update')
        author = form.cleaned_data.get('author')

        return  HttpResponseRedirect('/blog/questionResponse.html')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = ResponseForm()

        return render(request, 'questionResponse.html', {'form':form})"""




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
