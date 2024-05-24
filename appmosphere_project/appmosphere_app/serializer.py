from rest_framework import serializers 
from . models import Profilepage
from .models import Comment
from .models import Feed
  
class ProfilePageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Profilepage
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"

