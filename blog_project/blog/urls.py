"""
Blog URL Configuration
----------------------
This file maps URLs to views in the blog app.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page - list all posts
    # URL: /
    path('', views.home, name='home'),
    
    # View a single post
    # URL: /post/1/ (where 1 is the post ID)
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # Create a new post
    # URL: /post/new/
    path('post/new/', views.post_create, name='post_create'),
    
    # Edit an existing post
    # URL: /post/1/edit/ (where 1 is the post ID)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    # Delete a post
    # URL: /post/1/delete/ (where 1 is the post ID)
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
