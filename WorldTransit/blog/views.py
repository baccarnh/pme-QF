from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Questions, Response

def questionResponse(request):
    """request for search object in table and return objects in templates for display informations"""
    quest = Questions.objects.all()
    liste = list()
    liste.append(quest)

    resp = Response.objects.all()
    liste2 = list()
    liste2.append(resp)
    return render(request, 'blog/questionResponse.html', {'quest':liste, 'resp': liste2})

def handler404(request):
    return render(request,'errors/404.html',status=404)