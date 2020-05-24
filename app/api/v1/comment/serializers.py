from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment
from post.models import Post
from app.api.v1.user.serializers import UserSerializer


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)
    user = UserSerializer()

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = ["id", 'post', 'user', "content", "children"]


class CommentCreateSerializer(ModelSerializer):
    """Creation of comment, if no parent - its root comment, if parent exist - it`s  reply"""
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'parent']

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')
        return attrs


class CommentUpdateDeleteSerializer(ModelSerializer):
    """Update comment or delete"""

    class Meta:
        model = Comment
        fields = ['content']
