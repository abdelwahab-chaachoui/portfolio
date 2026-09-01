from django.urls import path, include
from rest_framework import routers
from .viewset import PostViewSet, KeywordViewSet  # , CommentForPostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'keywords', KeywordViewSet)

#router.register(r'comments/<post_id>', CommentForPostViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]

