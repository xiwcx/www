from django.contrib import admin

from .models import Image, Post, Work

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    fields = ('caption', 'upload',)
    readonly_fields = ('preview',)


class BaseContentAdmin(admin.ModelAdmin):
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        return obj.hero.preview()
    get_preview.short_description = 'Hero Preview'

class PostAdmin(BaseContentAdmin):
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "get_preview", "slug", "published_at", "status"]}),
    ]
    list_display = ("title", "get_preview", "published_at", "status")
    inlines = [ImageInline]

class WorkAdmin(BaseContentAdmin):
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "get_preview", "slug", "published_at", "type"]}),
    ]
    list_display = ("title", "get_preview", "published_at")
    inlines = [ImageInline]

admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Work, WorkAdmin)
