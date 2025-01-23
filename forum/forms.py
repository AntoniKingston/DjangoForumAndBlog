from django import forms
from . import models

class CreateThread(forms.ModelForm):
    class Meta:
        model = models.Thread
        fields = ['title']
class CreateThreadPost(forms.ModelForm):
    class Meta:
        model = models.ThreadPost
        fields = ['content']