from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields =  ['name', 'content', 'imdb', 'photo', 'cat']
        widgets = {
        'photo': forms.FileInput(attrs={'class': 'photo-input'}),
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Heç bir kateqoriya seçilməyib"



class ContactPostForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields =  ['name', 'email', 'suggest']
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
