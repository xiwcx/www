from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<slug:pk>/", views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
