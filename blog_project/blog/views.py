"""
Blog Views
----------
This file contains all the view functions for our blog app.
Each view handles a specific page or action.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


def home(request):
    """
    Home page view - displays a list of all blog posts.
    
    URL: /
    Template: home.html
    """
    # Get all posts from the database (ordered by created_at, newest first)
    posts = Post.objects.all()
    
    # Render the home template with the posts
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, pk):
    """
    Post detail view - displays a single blog post.
    
    URL: /post/<id>/
    Template: post_detail.html
    
    Args:
        pk: Primary key (ID) of the post to display
    """
    # Get the post with the given ID, or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    # Render the detail template with the post
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    """
    Create post view - displays a form to create a new blog post.
    
    URL: /post/new/
    Template: post_form.html
    
    Handles both GET (show form) and POST (save form) requests.
    """
    if request.method == 'POST':
        # User submitted the form - validate and save
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the new post to the database
            post = form.save()
            # Redirect to the detail page of the newly created post
            return redirect('post_detail', pk=post.pk)
    else:
        # User is viewing the form - create an empty form
        form = PostForm()
    
    # Render the form template
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Create'})


def post_edit(request, pk):
    """
    Edit post view - displays a form to edit an existing blog post.
    
    URL: /post/<id>/edit/
    Template: post_form.html
    
    Args:
        pk: Primary key (ID) of the post to edit
    """
    # Get the post to edit, or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        # User submitted the form - validate and save changes
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Update the post in the database
            form.save()
            # Redirect to the detail page of the updated post
            return redirect('post_detail', pk=post.pk)
    else:
        # User is viewing the form - populate it with existing post data
        form = PostForm(instance=post)
    
    # Render the form template
    return render(request, 'blog/post_form.html', {'form': form, 'action': 'Edit', 'post': post})


def post_delete(request, pk):
    """
    Delete post view - displays a confirmation page and deletes the post.
    
    URL: /post/<id>/delete/
    Template: post_confirm_delete.html
    
    Args:
        pk: Primary key (ID) of the post to delete
    """
    # Get the post to delete, or return 404 if not found
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        # User confirmed deletion - delete the post
        post.delete()
        # Redirect to the home page
        return redirect('home')
    
    # User is viewing the confirmation page
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
