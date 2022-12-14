from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .forms import PasswordChangeForm
# from .forms import PasswordChangeView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import NewsStory

class CreateAccountView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #slicing / news taking the first 4 stories as the latest stories 
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name = 'createAccount'
    template_name = 'users/createAccount.html'
    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.id})
    
class PasswordChangeView(PasswordChangeForm):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('news:index')
    
    