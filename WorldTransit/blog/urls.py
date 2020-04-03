from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('createaccount/', views.signup, name='createaccount'),
    path('questionResponse/', views.questionResponse, name='questionResponse'),
    path('newquestions/', views.questions, name='newquestions'),
    path('response/', views.response, name='response'),
]

