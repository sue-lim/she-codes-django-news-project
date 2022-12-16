from django.contrib import admin
from .models import NewsStory

class NewsStoryAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'pub_date', 'content',)
    ordering = ['title']
    search = ['title', 'content']
    actions = ['edit']


admin.site.register(NewsStory, NewsStoryAdmin)

# here we registered on the admin site a "NewsStory Model"

