from django.shortcuts import render, get_object_or_404
from django.http import Http404
from ..blog.models import Questions

def home(request):
    return render(request,'home.html' )


def login(request):
    return render(request,'pages/login.html')
