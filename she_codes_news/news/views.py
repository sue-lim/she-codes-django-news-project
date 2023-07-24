from django.views import generic
# same as above without havin to relist 
# from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# delays URL reversal until the actual URL is needed
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm, CommentForm
from django.shortcuts import get_object_or_404, redirect # 404 | redirection 
from django.contrib.auth.decorators import login_required #permission 
from django.core.exceptions import PermissionDenied #403 

class IndexView(generic.ListView):
    # pointin to where we want to use this
    template_name = 'news/index.html'
    def get_queryset(self):
        # return all stories
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        #super call parent class & adding customisation 
        context = super().get_context_data(**kwargs) 
        #slicing / news taking the first 4 stories as the latest stories 
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # displaying the rest if the stories by date max 4 to the page 
        context['all_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]
        return context

class AllStories(generic.ListView):
    template_name = 'news/allStories.html'
    def get_queryset(self):
        # return all stories
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:10]
        context['all_stories'] = NewsStory.objects.all().order_by('pub_date')[:10]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # includes the form in the story view 
        context["form"] = CommentForm()
        return context
    
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        # permissions | author is the user to add a story 
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "news/createComment.html"
    
    def form_valid(self, form):
        # author that is currently logged in will be the author of the comment
        form.instance.author = self.request.user
        # adding this to the story 
        pk = self.kwargs.get("pk")
        # retrieving this article and if not 404 
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        # saving this form as a new comment 
        return super().form_valid(form)
    
    # on update, return the page you have updated
    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    fields = ['title', 'pub_date','content' , 'image_url']
    context_object_name = "story"
    # once deleted, page will take you back to the index
    success_url = reverse_lazy('news:index')
    
    # the below is stating that unless you are the author you can not delete & 403 returned. 
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj

class EditStoryView(generic.UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'pub_date','content' , 'image_url']
    success_url = reverse_lazy('news:index')
    context_object_name = "story"
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied()
        return obj

# view to see each story by author 
# get a query set & filter by the author 
class AuthorStoriesView(generic.ListView):
    model = NewsStory
    template_name = 'news/profileStory.html'
    def get_queryset(self):
        q = super().get_queryset()
        qs = qs.filter(author_id=self.kwargs['pk']) 
        return qs
    
# reactions below for like / dislike / love 
# login required imported above 
@login_required
def like_post(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    # user is the login user and the one updating the like
    user = request.user
    if story.liked_by.filter(id=user.id).exists():
        story.liked_by.remove(user)
    else:
        story.liked_by.add(request.user)
    # adds & returns it to the story 
    return redirect('news:story', pk=story.id)

@login_required
def dislike_post(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    user = request.user
    if story.disliked_by.filter(id=user.id).exists():
        story.disliked_by.remove(user)
    else:
        story.disliked_by.add(request.user)
    
    return redirect('news:story', pk=story.id)

@login_required
def love_post(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    user = request.user
    if story.loved_by.filter(id=user.id).exists():
        story.loved_by.remove(user)
    else:
        story.loved_by.add(request.user)
    
    return redirect('news:story', pk=story.id)


