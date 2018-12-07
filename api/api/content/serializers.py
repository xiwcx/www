from rest_framework import serializers
from .models import Image, Post, Work


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("upload", "caption")


class BaseContentSerializer(serializers.HyperlinkedModelSerializer):
    hero = ImageSerializer()
    images = ImageSerializer(many=True)
    body = serializers.CharField()


class PostSerializer(BaseContentSerializer):
    class Meta:
        model = Post
        exclude = ("markdown", "status")


class WorkSerializer(BaseContentSerializer):
    class Meta:
        model = Work
        exclude = ("markdown",)
