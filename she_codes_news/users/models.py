from django.contrib.auth.models import AbstractUser
from django.db import models

#the below are additional user/fields.py I have added to the form for creating account and fields for updating the form. This is reflected in the user/models.py
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, blank=True)  # 
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.URLField('Profile picture URL', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    
    pass
    def __str__(self):
        return self.username


    # def __str__(self):
    #     return "Profile of {}".format(self.user.username)
        
########################################
# Here we are creating a model (a table in our future database) that inherits all the fields from the AbstractUser class (that's the built-in model that has fields like username, email, password, etc.), but we are also adding a couple of fields that aren't there. In this example, we are adding "First Name", "Last Name" and "Twitter Handle" fields.

# Once you are done setting this up, you can add more stuff, like Date of Birth, Profile Picture, other social links, or anything that your heart desires.

# As you can see we named this model CustomUser, which is what we are referring to in the last line of settings.py.