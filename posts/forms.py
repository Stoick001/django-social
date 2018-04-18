from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('message', 'group')

        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'})
        }
