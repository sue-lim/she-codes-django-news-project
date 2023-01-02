from audioop import reverse
from django.contrib.auth import get_user_model
from django.db import models

# basic admin panel with Groups and Users models which come from Django authentication framework located in django.contrib.auth.
User = get_user_model()

# this is the model
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Date of Story')
    content = models.TextField('Story')
    image_url = models.URLField(blank=True)
    loved_by = models.ManyToManyField(User, related_name='loved_stories', blank=True, null=True ) 
    liked_by = models.ManyToManyField(User, related_name='liked_stories', blank=True, null=True ) 
    disliked_by = models.ManyToManyField(User, related_name='disliked_stories', blank=True, null=True ) 
#text field for longer text vs such as blogs

def get_absolute_url(self):
    return reverse('news:story', kwargs={'pk': self.pk})

class Comment(models.Model):
    story = models.ForeignKey(NewsStory, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE
    )
    content = models.TextField('Comment', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    