#for working out with Django Admin, we now need a URL through which we can access our Admin Site
#Register Admin urls to our urls.py

from django.contrib import admin
from django.urls import path
from . views import IndexView, AllStories, StoryView, AddStoryView, EditStoryView, DeleteStoryView, AuthorStoriesView, AddCommentView
from . import views


app_name = 'news'

urlpatterns = [
    # homepage with sliced views 
    path('', IndexView.as_view(), name='index'),
    #page with all stories 
    path('allStories/', AllStories.as_view(), name='allStories'),
    #view seperate stories 
    path('<int:pk>/', StoryView.as_view(), name='story'),
    #view add story page, no int pk for post a story as there is no story yet
    path('addStory/', AddStoryView.as_view(), name='newStory'),
    #  edit story 
    path('<int:pk>/editStory/', EditStoryView.as_view(), name='editStory'),
    # delete story 
    path('<int:pk>/deleteStory/', DeleteStoryView.as_view(), name='deleteStory'),
    # view stories under the user 
    path('<int:pk>/authorStories/', AuthorStoriesView.as_view(), name='profileStory'),
    # add comment to a story 
    path('<int:pk>/comment/', AddCommentView.as_view(), name='addComment'),
    # update like to a story 
    path('<int:pk>/like', views.like_post, name="like"),
    # update dislike to a story 
    path('<int:pk>/dislike', views.dislike_post, name="dislike"),
    # update love to a story 
    path('<int:pk>/love', views.love_post, name="love"),


]
