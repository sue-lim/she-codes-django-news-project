from django.urls import path
from .views import CreateAccountView, EditAccountView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('create-account/edit', EditAccountView.as_view(), name='editAccount'),
]