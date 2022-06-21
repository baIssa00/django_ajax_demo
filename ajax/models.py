from pyexpat import model
from django.db import models
from django.forms import PasswordInput

class Post (models.Model):
    email = models.EmailField()
    password = models.TextField(PasswordInput)

    def __str__(self):
        return self.email