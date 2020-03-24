from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions, Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import SuccessURLAllowedHostsMixin, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login


class LoginView(SuccessURLAllowedHostsMixin, FormView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = 'templates/login.html'


def home(request):
    quest = Questions.objects.all()
    liste = list()
    liste.append(quest)
    return render(request, 'blog/home.html', {'quest': liste})



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

"""def signout(request):
    logout(request)
    return redirect('login')"""
def questionResponse(request):
    """request for search object in table and return objects in templates for display informations"""
    quest = get_object_or_404(Questions, id=1)
    liste = list()
    liste.append(quest)

    resp = Response.objects.filter(user_id=1)
    liste2 = list()
    liste2.append(resp)
    return render(request, 'blog/questionResponse.html', {'quest':liste, 'resp': liste2})

def handler404(request):
    return render(request,'errors/404.html',status=404)