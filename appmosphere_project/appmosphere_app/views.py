from django.shortcuts import render
from .models import Profilepage
from pymongo import MongoClient
from . serializer import ProfilePageSerializer
from rest_framework import viewsets

from rest_framework.response import Response


client = MongoClient('URI')

class ProfilePageViewSet(viewsets.ModelViewSet):
    queryset = Profilepage.objects.all()
    serializer_class = ProfilePageSerializer




