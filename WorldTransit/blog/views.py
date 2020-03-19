from django.shortcuts import render


def questionResponse(request):
    return render(request,'questionResponse.html')