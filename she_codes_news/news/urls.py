#for working out with Django Admin, we now need a URL through which we can access our Admin Site
#Register Admin urls to our urls.py

from django.contrib import admin
from django.urls import path
from . import views
from .views import EditStoryView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('post/edit/<int:pk>/', EditStoryView.as_view(), name='editStory'),
]
