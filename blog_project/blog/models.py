"""
Blog Models
-----------
This file defines the database structure for our blog.
"""

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Post model represents a blog post.
    
    Fields:
    - title: The title of the blog post (max 200 characters)
    - content: The main content/body of the blog post (unlimited text)
    - created_at: Timestamp when the post was created (auto-set)
    """
    
    # Title field - limited to 200 characters
    title = models.CharField(max_length=200)
    
    # Content field - can hold large amounts of text
    content = models.TextField()
    
    # Created timestamp - automatically set when post is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Order posts by creation date, newest first
        ordering = ['-created_at']
    
    def __str__(self):
        """
        String representation of the post.
        Returns the title when the object is printed.
        """
        return self.title
