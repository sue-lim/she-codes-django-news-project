from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name',  'email', 'bio' , 'profile_picture', 'linkedin', 'instagram' ]
        
        widgets = {
            'username' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            'first_name' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            'last_name' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            'bio' : forms.Textarea({'size': '45','placeholder' : 'Tell us more about yourself......'}),
            'profile_picture' : forms.URLInput({'size': '45','placeholder' : 'https://...'}),
            'email' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            'linkedin' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            'instagram' : forms.TextInput({'size': '45','size': '45','placeholder' : ''}),
            }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name', 'last_name',  'email', 'bio' , 'profile_picture']
        

