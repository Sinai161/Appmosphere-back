from django.shortcuts import render
from .models import Profilepage, Comment, Feed, User
from pymongo import MongoClient
from . serializer import ProfilePageSerializer, CommentSerializer, FeedSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import os


# client = MongoClient(os.environ.get('URI'))
# db = client['appmosphere_db']

class ProfilePageViewSet(viewsets.ModelViewSet):
    queryset = Profilepage.objects.all()
    serializer_class = ProfilePageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

# API view for django.contrib.auth.models.User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
  



