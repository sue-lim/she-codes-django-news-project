from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    bio = models.CharField(max_length=20, blank=True)
    email = models.TextField(blank= True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    
    pass
    def __str__(self):
        return self.username


        def __str__(self):
            return "Profile of {}".format(self.user.username)
        
########################################
# Here we are creating a model (a table in our future database) that inherits all the fields from the AbstractUser class (that's the built-in model that has fields like username, email, password, etc.), but we are also adding a couple of fields that aren't there. In this example, we are adding "First Name", "Last Name" and "Twitter Handle" fields.

# Once you are done setting this up, you can add more stuff, like Date of Birth, Profile Picture, other social links, or anything that your heart desires.

# As you can see we named this model CustomUser, which is what we are referring to in the last line of settings.py.