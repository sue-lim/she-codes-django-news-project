#for working out with Django Admin, we now need a URL through which we can access our Admin Site
#Register Admin urls to our urls.py

from django.contrib import admin
from django.urls import path
from . views import IndexView, AllStories, StoryView, AddStoryView, EditStoryView, DeleteStoryView, AuthorStoriesView, AddCommentView


app_name = 'news'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', AllStories.as_view(), name='allStories'),
    path('<int:pk>/post/', StoryView.as_view(), name='story'),
    path('add-story/', AddStoryView.as_view(), name='newStory'),
    # no int pk for post a story as there is no story yet 
    path('editStory/<int:pk>/', EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/deleteStory/', DeleteStoryView.as_view(), name='deleteStory'),
    path('<int:pk>/', AuthorStoriesView.as_view(), name='profileStory'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='addComment'),
]
