from django.views import generic
from .models import NewsStory


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        #slicing / news taking the first 4 stories as the latest stories 
        context['all_stories'] = NewsStory.objects.all()
        return context

#class based view 
