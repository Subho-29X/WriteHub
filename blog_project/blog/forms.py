"""
Blog Forms
----------
This file defines forms for creating and editing blog posts.
"""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts.
    
    Uses Django's ModelForm to automatically create form fields
    based on the Post model.
    """
    
    class Meta:
        model = Post
        # Include only title and content fields
        # (created_at is auto-generated, so we don't need it in the form)
        fields = ['title', 'content']
        
        # Add helpful labels and placeholders
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter a catchy title...',
                'size': '50'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your blog post here...',
                'rows': 10,
                'cols': 50
            }),
        }
