from django.db import models
"""class for 3 tables Users, Questions, Answers"""

class Users(models.Model):
    name = models.CharField(max_length=255,default=None)
    last_name = models.CharField(max_length=255,default=None)
    pseudo = models.CharField(max_length=255,default=None)
    job = models.CharField(max_length=255,default=None)
    password = models.CharField(max_length=255,default=None)

    def __str__(self):
        return f'name({self.name}),last_name({self.last_name}),pseudo({self.pseudo})'


class Questions(models.Model):
    title = models.CharField(max_length=255,default=None)
    content = models.TextField(default=None)
    publishing_date = models.DateTimeField(default=None)
    author = models.CharField(max_length=255,default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE,default=None)


class Answers(models.Model):
    content = models.TextField(default=None)
    publishing_date = models.DateTimeField(default=None)
    author = models.CharField(max_length=255, default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)

