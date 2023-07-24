# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

#the lines below add the fields to the main admin page, if I have created additional classed in models. I can add them here to update the admin in http://127.0.0.1:8000/admin/
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name', 'email', 'date_joined' ,'last_login', 'profile_picture']
    action = ['edit']
    fieldsets = UserAdmin.fieldsets 

admin.site.register(CustomUser, CustomUserAdmin)