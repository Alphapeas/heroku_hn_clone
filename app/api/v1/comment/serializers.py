from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from comment.models import Comment
from post.models import Post
from app.api.v1.user.serializers import UserSerializer


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


class PostCommentSerializer(ModelSerializer):
    """Post comments"""
    user = UserSerializer()
    parent = serializers.CharField()

    class Meta:
        model = Post
        fields = ['id', 'content', 'user', 'parent']


class CommentChildSerializers(ModelSerializer):
    """Child comments is comments where parent is not null"""
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'parent']


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    user = UserSerializer()
    post = PostCommentSerializer()

    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'replies']

    def get_replies(self, obj):
        if obj.any_children:
            return CommentChildSerializers(obj.children(), many=True).data


class CommentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']
