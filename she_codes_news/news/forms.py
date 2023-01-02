from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
from django.forms import TextInput, EmailInput, Textarea


class StoryForm(forms.ModelForm):
    class Meta:
        model = NewsStory
        # you can re-order the below
        fields = ['title', 'pub_date', 'content', 'image_url']
        widgets = {
            'title' : forms.TextInput({'size': '45','placeholder' : 'Enter the title of your story here...'}),
            'pub_date' : forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control','type':'date' }),
            'content' : forms.Textarea({'size': '45','placeholder' : 'Enter your story here...'}),
            'image_url' : forms.URLInput({'size': '45','placeholder' : 'https://...'}),
            }
        
        
#         {
#             'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
# }
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
        # you can re-order the below
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
        
