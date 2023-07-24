from django.urls import path
from .views import CreateAccountView,  ProfileView, EditAccountView, PasswordChangeView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('createAccount/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/edit/', EditAccountView.as_view(), name='editAccount'),
    # path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),
]