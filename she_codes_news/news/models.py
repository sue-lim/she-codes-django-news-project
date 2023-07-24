from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# django inbuilt function, which we have imported above. It returns active users for the current model.
# this has been set in settings.py 
User = get_user_model()

# Defining the newsstory model 
class NewsStory(models.Model):
    # fields 
    title = models.CharField(max_length=200)
    # fk links this back to the user 
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date of Story')
    content = models.TextField('Story')
    image_url = models.URLField(blank=True)

    # possible to rewrite as a class reaction vs the longer way below.
    # Many-to-many relationships for user reactions to news stories
    loved_by = models.ManyToManyField(User, related_name='loved_stories', blank=True, null=True ) 
    liked_by = models.ManyToManyField(User, related_name='liked_stories', blank=True, null=True ) 
    disliked_by = models.ManyToManyField(User, related_name='disliked_stories', blank=True, null=True ) 

    # Method to get the absolute URL for a NewsStory instance
    # Which means when you click on it it will take you to the details of that stiry 
    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})

# Defining the newsstory model 
class Comment(models.Model):
    # fields 
    # foreign key that links the comments to the newstory model
    story = models.ForeignKey(NewsStory, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE
    )
    content = models.TextField('Comment', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    