from django.conf.urls import url, include, re_path
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('login/', views.connexion, name='login'),
    path('login/', views.deconnexion, name='login'),
    path('createaccount/', views.signup, name='createaccount'),
    path('questionResponse/', views.questionResponse, name='questionResponse'),
    path('useraccount/', views.useraccount, name='useraccount'),
    path('newquestions/', views.questions, name='newquestions'),
]

#url(r'^$', views.home, name='home'),
#url(r'^', views.login, name='login'),
#url(r'^',views.questionResponse,name='questionResponse'),
#url(r'^', views.createaccount, name='createaccount'),