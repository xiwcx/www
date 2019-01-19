"""
API URLs
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(
    url=staticfiles_storage.url("favicon.ico"), permanent=False
)


def index(request):
    """Render index"""
    return render(request, "index.html")


urlpatterns = [
    path("v1/", include("content.urls")),
    path("admin/", admin.site.urls),
    url(r"^favicon.ico$", favicon_view, name="favicon"),
    url(r"^$", index),
]
