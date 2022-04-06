from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Profile, Skill, Message
from django.forms.widgets import TextInput, Textarea, EmailInput


# =================================
# Custom User Creation View
# =================================
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        unique_together = ('email',)


# =================================
# Edit Profile View
# =================================
class editProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'featured_image', 'short_intro', 'location',
                  'github_link', 'stackoverflow_link', 'twitter_link', 'linkedin_link', 'website_link']


# =================================
# Edit Profile View
# =================================
class skillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        widgets = {
            'description': Textarea(attrs={'rows': 4}),
        }


# =================================
# Create Message View
# =================================
class messageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
