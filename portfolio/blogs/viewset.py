from rest_framework import viewsets
from blogs.serializers import PostSerializer, KeywordSerializer
from blogs.models import Post, Keyword

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=2)
    serializer_class = PostSerializer

class ArchivedPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=3)
    serializer_class = PostSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
