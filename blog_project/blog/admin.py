"""
Blog Admin Configuration
------------------------
This file registers our models with Django's admin interface.
"""

from django.contrib import admin
from .models import Post


# Register the Post model with the admin site
# This allows us to manage blog posts through the Django admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customize how posts appear in the admin interface.
    """
    # Display these fields in the admin list view
    list_display = ('title', 'created_at')
    
    # Add filters for easy sorting
    list_filter = ('created_at',)
    
    # Add search functionality
    search_fields = ('title', 'content')
    
    # Make created_at read-only (it's auto-generated)
    readonly_fields = ('created_at',)
