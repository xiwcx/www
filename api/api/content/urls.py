from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", views.PostViewSet)
router.register(r"works", views.WorkViewSet)

urlpatterns = [path("", include(router.urls))]
