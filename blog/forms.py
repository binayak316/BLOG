from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogModel, ProfileModel
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class BlogModelForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write a title for your Blog'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'Write Your Blog or an Article....'}))
    class Meta:
        model = BlogModel
        fields = ['title', 'content','image']#image ne rakhne

class ProfileModelForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'Update your Bio'}))
    class Meta:
        model = ProfileModel
        fields = ['image','bio'] #image in upload huna paryo profile picture

class PostUpdateForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write a title for your Blog'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'Write Your Blog or an Article....'}))
    class Meta:
        model = BlogModel
        fields = ['title', 'content','image']

      