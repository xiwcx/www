"""
content models
"""

from django.db import models
from django.utils import timezone
from .utils import HighlightRenderer
import mistune
from django.utils.safestring import mark_safe


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


class Image(models.Model):
    caption = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

    def preview(self):
        return mark_safe('<img class="image-preview" src="{0}">'.format(self.upload.url))

    def __str__(self):
        return self.caption

class RelatedImage(Image):
    images = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name="images")

# Create your models here.
class Post(models.Model):
    """Post model"""

    markdown = models.TextField()
    hero = models.OneToOneField(
        Image, blank=True, null=True, on_delete=models.CASCADE, related_name="hero"
    )
    pub_date = models.DateTimeField("date published", default=timezone.now)
    published = models.BooleanField(default=False)
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=500)

    class Meta:
        db_table = "post"

    def __str__(self):
        return self.title

    def body(self):
        return markdown(self.markdown)
