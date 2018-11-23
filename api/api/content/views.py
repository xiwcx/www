from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
