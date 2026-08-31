from rest_framework import serializers
from blogs.models import Post, Comment

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'date', 'tags', 'author', 'status', 'keywords')

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'content', 'date', 'author', 'active', 'email')
