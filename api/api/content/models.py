"""
content models
"""

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """Post model"""

    body = models.TextField()
    pub_date = models.DateTimeField("date published", default=timezone.now)
    published = models.BooleanField(default=False)
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=500)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title


class Image(models.Model):
    caption = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

    def __str__(self):
        return self.caption
