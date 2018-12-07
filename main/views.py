from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = PostSerializer