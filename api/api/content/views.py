"""
content views
"""

from rest_framework import generics
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer


class PostDetail(generics.RetrieveAPIView):
    """Post list create API view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostList(generics.ListCreateAPIView):
    """Post list create API view"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
