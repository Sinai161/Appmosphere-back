from rest_framework import serializers 
from . models import Profilepage
from .models import Comment
  
class ProfilePageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Profilepage
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'