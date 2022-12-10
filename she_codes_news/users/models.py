from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username


        def __str__(self):
            return "Profile of {}".format(self.user.username)