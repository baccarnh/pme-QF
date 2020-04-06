from django.db import models
"""class for 3 tables Users, Questions, Answers"""

class Users(models.Model):
    name = models.CharField(max_length=255,default=None)
    last_name = models.CharField(max_length=255,default=None)
    pseudo = models.CharField(max_length=255,default=None)
    job = models.CharField(max_length=255,default=None)
    password = models.CharField(max_length=255,default=None)




class Questions(models.Model):
    title = models.CharField(max_length=250,default=None)
    content = models.TextField(default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255,default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,default=None)
    status = models.BooleanField(null=True)




class Response(models.Model):
    title = models.CharField(max_length=255,default=None)
    content = models.TextField(default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255,default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,default=None)
    bases = (models.Model),





