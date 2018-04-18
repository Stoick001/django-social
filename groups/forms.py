from django import forms
from .models import Group

class CreateGroupForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = ('name', 'description')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-8'})
        }
