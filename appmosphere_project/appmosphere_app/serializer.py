from rest_framework import serializers 
from .models import Profilepage
from .models import Comment
from .models import Feed
from .models import User
MIN_LENGTH = 7

class ProfilePageSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Profilepage
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            'min_length': f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            'min_length': f"Password must be longer than {MIN_LENGTH}"
        }
    )

    class Meta:     
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data["username"],
        email=validated_data["email"],
    )

        user.make_password(validated_data["password"])
        user.save()

        return user