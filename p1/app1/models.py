from django.db import models
from django.db.models import Model


# Create your models here.

class UserModel(Model):
    username = models.CharField(max_length=100)
    fruit = models.CharField(max_length=10)
    vegetables = models.CharField(max_length=100)
