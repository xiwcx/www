"""
content models
"""

import mistune
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from .utils import HighlightRenderer

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)

# Image Types
class Image(models.Model):
    caption = models.CharField(max_length=500)
    height = models.IntegerField()
    related_post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, blank=True, null=True, related_name="images"
    )
    related_work = models.ForeignKey(
        "Work", on_delete=models.CASCADE, blank=True, null=True, related_name="images"
    )
    upload = models.ImageField(height_field="height", width_field="width")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField()

    class Meta:
        db_table = "image"

    def preview(self):
        url = self.upload.url

        if url:
            return mark_safe(
                '<img class="image-preview" src="{0}">'.format(self.upload.url)
            )

        return None

    def __str__(self):
        return self.caption


# Content Types
class ContentBase(models.Model):
    """Base Content Abstract Model"""

    hero = models.OneToOneField(Image, blank=True, null=True, on_delete=models.CASCADE)
    markdown = models.TextField()
    published_at = models.DateTimeField("date published", default=timezone.now)
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def body(self):
        return markdown(self.markdown)


class Post(ContentBase):
    DRAFT = "draft"
    PUBLISHED = "published"
    POST_STATUS_CHOICES = ((DRAFT, "Draft"), (PUBLISHED, "Published"))

    status = models.CharField(max_length=20, choices=POST_STATUS_CHOICES, default=DRAFT)

    class Meta:
        db_table = "post"


class Work(ContentBase):
    ART = "art"
    CODE = "code"
    WORK_TYPE_CHOICES = ((CODE, "Code"), (ART, "Art"))

    type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES, default=None)

    class Meta:
        db_table = "work"
