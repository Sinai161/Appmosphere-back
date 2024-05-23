from rest_framework import serializers 
from . models import Profilepage
  
class ProfilePageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Profilepage
        fields = '__all__'