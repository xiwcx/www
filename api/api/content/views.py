"""
content views
"""

from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Post list create API view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
