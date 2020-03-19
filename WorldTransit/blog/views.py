from django.shortcuts import render


def questionResponse(request):
    post = ['sofiane','nicos','nour']
    return render(request,'blog/questionResponse.html',{'posts':post})