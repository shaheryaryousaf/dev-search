from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio', 'user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'title': TextInput(attrs={'placeholder': 'Project Title'}),
            'demo_link': TextInput(attrs={'placeholder': 'Demo Link'}),
            'source_link': TextInput(attrs={'placeholder': 'Source Link'}),
            'description': Textarea(attrs={'placeholder': 'Description', 'rows': 4}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

        widgets = {
            'body': Textarea(attrs={'rows': 4}),
        }
