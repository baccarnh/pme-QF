from django.shortcuts import render

from blog.models import Users


def questionResponse(request):
    users = Users.objects.all()
    return render(request,'blog/questionResponse.html',{'users':users})