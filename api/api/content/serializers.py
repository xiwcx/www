from rest_framework import serializers
from .models import Image, Post


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("upload", "caption")


class PostSerializer(serializers.HyperlinkedModelSerializer):
    hero = ImageSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Post
        exclude = ("published",)
