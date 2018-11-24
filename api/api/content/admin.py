from django.contrib import admin

from .models import Image, Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "images", "slug", "pub_date", "published"]}),
    ]
    list_display = ("title", "pub_date", "published")


admin.site.register(Image)
admin.site.register(Post, PostAdmin)
