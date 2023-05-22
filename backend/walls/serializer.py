# walls/serializer.py
from rest_framework import serializers
from walls.models import User,Post,Comment

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'