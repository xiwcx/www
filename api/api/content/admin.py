from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "body"]}),
        ("Meta", {"fields": ["slug", "hero", "pub_date", "published"]}),
    ]
    list_display = ("title", "pub_date", "published")


admin.site.register(Post, PostAdmin)
