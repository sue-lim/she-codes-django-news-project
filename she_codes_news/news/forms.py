from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import NewsStory, Comment
# calling the objects from the model and reusing them below 



class StoryForm(forms.ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'title' : forms.TextInput({'size': '45','placeholder' : 'Enter the title of your story here...'}),
            'pub_date' : forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control','type':'date' }),
            'content' : forms.Textarea({'size': '45','placeholder' : 'Enter your story here...'}),
            'image_url' : forms.URLInput({'size': '45','placeholder' : 'https://...'}),
            }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        # you can re-order the below
        
# class DeleteStory(forms.ModelForm):
#     class Meta:
#         model = DeleteStory
#         fields = ['content']
#         # you can re-order the below
        
class EditStory(forms.ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'size: 300px;'
                }),
            'pub_date' : forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control','type':'date' }),
            'content' : forms.Textarea(),
            'image_url' : forms.URLInput(attrs={'class': 'form_area_test'}),
            }
        
