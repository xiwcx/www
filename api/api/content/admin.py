from django.contrib import admin

from .models import Image, RelatedImage, Post

class ImageInline(admin.StackedInline):
    model = RelatedImage
    extra = 1
    readonly_fields = ('preview',)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('get_preview',)
    fieldsets = [
        (None, {"fields": ["title", "markdown"]}),
        ("Meta", {"fields": ["hero", "get_preview", "slug", "pub_date", "published"]}),
    ]
    list_display = ("title", "get_preview", "pub_date", "published")
    inlines = [ImageInline]

    def get_preview(self, obj):
        return obj.hero.preview()
    get_preview.short_description = 'Hero'


admin.site.register(Image)
admin.site.register(RelatedImage)
admin.site.register(Post, PostAdmin)
