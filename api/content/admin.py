"""
content admin settings
"""

from django.contrib import admin

from .models import Image, Post, Work


class ImageAdmin(admin.ModelAdmin):
    """Image admin"""
    fieldsets = [
        (None, {"fields": ["upload", "caption"]}),
        ("Relationships", {"fields": ["related_post", "related_work"]}),
        ("Meta", {"fields": ["preview", "height", "width", "uploaded_at"]}),
    ]
    readonly_fields = ("preview", "height", "width", "uploaded_at")


class ImageInline(admin.StackedInline):
    """Image inline admin"""
    model = Image
    extra = 1
    fields = ("caption", "upload")
    readonly_fields = ("height", "preview", "width")


class BaseContentAdmin(admin.ModelAdmin):
    """Base content admin"""
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        hero = obj.hero

        if hero:
            return obj.hero.preview()
        return None

    get_preview.short_description = "Hero Preview"


class PostAdmin(BaseContentAdmin):
    """Post admin"""
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "get_preview", "slug", "published_at", "status"]}),
    ]
    list_display = ("title", "get_preview", "published_at", "status")
    inlines = [ImageInline]


class WorkAdmin(BaseContentAdmin):
    """Work admin"""
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "get_preview", "slug", "published_at", "type"]}),
    ]
    list_display = ("title", "get_preview", "published_at")
    inlines = [ImageInline]


admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Work, WorkAdmin)
