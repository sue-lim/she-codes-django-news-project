from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DeleteView
# from django.core.exceptions import PermissionDenied




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

class AllStories(generic.ListView):
    template_name = 'news/allStories.html'

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        # this is the user that is currently logged in
        return super().form_valid(form)
    
class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/createComment.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})
    
################# need to sort the below #################
class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    context_object_name = "story"
    success_url = reverse_lazy('news:index')
    
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     if obj.author != self.request.user:
    #         raise PermissionDenied()
    #     return obj
    
# the below adds the view to update the story and links to updateStory.html
class EditStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'pub_date','content' , 'image_url']
    success_url = reverse_lazy('news:index')
    # context_object_name = "story"
    
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     if obj.author != self.request.user:
    #         raise PermissionDenied()
    #     return obj

class AuthorStoriesView(ListView):
    model = NewsStory
    template_name = 'news/profileStory.html'
    def get_queryset(self):
        """get the new stories for the author specified in the URL"""
        qs = super().get_queryset()  # get default queryset
        qs = qs.filter(author_id=self.kwargs['pk'])  # add filter for only the user you / authors id care about
        return qs
    

    

