from rest_framework import serializers
from .models import Image, Post, Work


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.CharField(source='upload.url', read_only=True)

    class Meta:
        model = Image
        fields = ("src", "caption", "width", "height")


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
