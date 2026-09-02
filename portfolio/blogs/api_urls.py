from django.urls import path, include
from rest_framework import routers
from .viewset import PostViewSet, KeywordViewSet, ArchivedPostViewSet  # , CommentForPostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'keywords', KeywordViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]

