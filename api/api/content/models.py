"""
content models
"""

from django.db import models
from django.utils import timezone


class Image(models.Model):
    caption = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

    def __str__(self):
        return self.caption


# Create your models here.
class Post(models.Model):
    """Post model"""

    body = models.TextField()
    hero = models.OneToOneField(
        Image, blank=True, on_delete=models.CASCADE, null=True, related_name="hero"
    )
    images = models.ManyToManyField(Image, related_name="images")
    pub_date = models.DateTimeField("date published", default=timezone.now)
    published = models.BooleanField(default=False)
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=500)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title
