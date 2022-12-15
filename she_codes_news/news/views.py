from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        #slicing / news taking the first 4 stories as the latest stories 
        context['all_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]
        return context

#class based view 
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # this is the user that is currently logged in
        return super().form_valid(form)
    
# the below adds the view to update the story and links to updateStory.html
class EditStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'content', 'author' , 'image_url']

class AuthorStoriesView(ListView):
    model = NewsStory
    template_name = 'news/profileStory.html'
    context_object_name = 'profileStory'
    # def get_queryset(self):
    #     # return NewsStory.objects.all()
    #     return NewsStory.objects.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context                                                
    
    
    
    
    
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #slicing / news taking the first 4 stories as the latest stories 
    #     # context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
    #     context['author_stories'] = NewsStory.objects.filter(author='author')
    #     return context

