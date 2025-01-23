from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields=['title', 'content']
class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields=['content']
class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title']