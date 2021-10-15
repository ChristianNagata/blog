from django import forms
from django.db.models import fields
from .models import BlogPost
from blog_added import models


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Text'}
