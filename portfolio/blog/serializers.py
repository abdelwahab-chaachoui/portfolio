from rest_framework import serializers
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    content = serializers.TextField(required=True)
    date = serializers.DateField(required=True)
    keywords = serializers.CharField(required=False)
    tags = serializers.CharField(required=False)
    author = serializers.CharField(required=True)
    status = serializers.BooleanField(required=False)  # published or not