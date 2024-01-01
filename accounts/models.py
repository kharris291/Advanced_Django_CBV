from django.contrib.auth.models import User as AuthUser, PermissionsMixin
from django.db import models
from django.contrib import auth


# Create your models here.
class User(AuthUser, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
