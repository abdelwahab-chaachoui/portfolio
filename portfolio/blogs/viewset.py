from rest_framework import viewsets
from blogs.serializers import PostSerializer, CommentSerializer, KeywordSerializer
from blogs.models import Post, Comment, Keyword

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

#class CommentForPostViewSet(viewsets.ModelViewSet,):
    #blog = Post.objects.get(id=post_id)
    #queryset = blog.comments.all()
    #serializer_class = CommentSerializer