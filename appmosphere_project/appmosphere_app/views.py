from django.shortcuts import render
from .models import Profilepage, Comment, Feed, User
from . serializer import ProfilePageSerializer, CommentSerializer, FeedSerializer, MyTokenObtainPairSerializer,RegisterSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class ProfilePageViewSet(viewsets.ModelViewSet):
    queryset = Profilepage.objects.all()
    serializer_class = ProfilePageSerializer
    # permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    # permission_classes = [IsAuthenticated]

# API view for django.contrib.auth.models.User
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class MyObtainTokenPairViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
