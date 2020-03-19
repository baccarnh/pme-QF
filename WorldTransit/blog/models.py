from django.db import models


class Users(models.Model):

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pseudo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Questions(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    publishing_date = models.DateTimeField()
    author = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
