from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

        self.fields['username'].widget.attrs['class'] = 'form-control col-md-6'
        self.fields['email'].widget.attrs['class'] = 'form-control col-md-6'
        self.fields['password1'].widget.attrs['class'] = 'form-control col-md-6'
        self.fields['password2'].widget.attrs['class'] = 'form-control col-md-6'

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control col-md-6'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control col-md-6', 'type': 'password'}))
