from django.shortcuts import render, redirect
from blog.models import Questions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
#user = authenticate(username='john', password='secret')


def home(request):
    quest = Questions.objects.all()
    liste = list()
    liste.append(quest)
    return render(request, 'home.html', {'quest': liste})



#def login(request):
    #return render(request,'pages/login.html')

def login(request):
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
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('login')