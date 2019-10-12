from .models import Comment, CommentReply, Post
from django.forms import ModelForm, ImageField, FileField
from PIL import Image
from django import forms
from django.core.files.images import get_image_dimensions
from django.core.files import File
from simple_search import search_form_factory


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'date_posted', 'content', 'image_2', 'category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class CommentReplyForm(ModelForm):
    class Meta:
        model = CommentReply
        fields = ['message']
