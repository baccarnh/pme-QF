from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Users


def questionResponse(request):

    """try:
        users = Users.objects.get(id=15)
        liste = list()
        liste.append(users)
    except:
        raise Http404('id n''esxiste pas')"""
    users = get_object_or_404(Users,id=1)
    liste = list()
    liste.append(users)
    return render(request,'blog/questionResponse.html',{'users':liste})


def handler404(request):
    return render(request,'errors/404.html',status=404)