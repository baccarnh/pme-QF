from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^$',views.questionResponse,name='questionResponse'),
    url(r'^',views.home,name='home'),

]