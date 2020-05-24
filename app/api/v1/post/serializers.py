from rest_framework import serializers

from post.models import Post
from app.api.v1.user.serializers import UserSerializer
from app.api.v1.comment.serializers import CommentSerializer


class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'link', 'content', 'rating']


class PostCUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'link', 'user']


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'link', 'comments', 'content', 'rating']
