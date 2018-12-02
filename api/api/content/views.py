"""
content views
"""

from rest_framework import viewsets
from rest_framework import permissions

from .models import Post, Work
from .serializers import PostSerializer, WorkSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """Post list create API view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    """Post list create API view"""

    queryset = Work.objects.all()
    serializer_class = WorkSerializer
