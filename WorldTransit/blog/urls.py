from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^', views.login, name='login'),
    url(r'^questionResponse/',views.questionResponse,name='questionResponse'),
    url(r'^createaccount', views.createaccount, name='createaccount'),
]