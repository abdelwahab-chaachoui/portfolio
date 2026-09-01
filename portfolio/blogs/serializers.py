from rest_framework import serializers
from blogs.models import Post, Comment, Keyword, Image

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(read_only=True)
    tags = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'date', 'tags', 'author', 'status', 'keywords', 'comments', 'images')

    def get_tags(self, obj):
        return obj.tags.split(' ')

    def get_comments(self, obj):
        comments = obj.comments.filter(active=True)
        return CommentSerializer(comments, many=True).data