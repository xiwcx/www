"""
content views
"""

from rest_framework import viewsets
from rest_framework import permissions
from django.utils import timezone

from .models import Post, Work
from .serializers import PostSerializer, WorkSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Post list create API view"""

    queryset = Post.objects.filter(
        status="published", published_at__lte=timezone.now()
    ).order_by("-published_at")
    serializer_class = PostSerializer


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    """Post list create API view"""

    queryset = Work.objects.filter(published_at__lte=timezone.now()).order_by(
        "-published_at"
    )
    serializer_class = WorkSerializer
