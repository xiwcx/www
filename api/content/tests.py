from django.test import TestCase

from .models import Post, Work

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.utils import timezone
from datetime import timedelta

from content import views


class PostModelTests(TestCase):
    def test_base_content_type_translates_markdown_to_html(self):
        """
        test that the body property is properly translated to html from markdown
        """

        a_post = Post(markdown="*test*")
        self.assertEqual(a_post.body(), "<p><em>test</em></p>\n")


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PostViewSet.as_view({"get": "list"})
        self.uri = "/posts/"
        Post.objects.create(
            slug="draft",
            title="Draft",
            status="draft",
            published_at=timezone.now() - timedelta(hours=2),
        )
        Post.objects.create(
            slug="published",
            title="Published",
            status="published",
            published_at=timezone.now() - timedelta(hours=2),
        )
        Post.objects.create(
            slug="published-future",
            title="Published Future",
            status="published",
            published_at=timezone.now() + timedelta(hours=2),
        )

    def test_list_filter(self):
        request = self.factory.get(self.uri)
        response = self.view(request)

        self.assertEqual(Post.objects.count(), 3, "Expected to find 3 saved posts")

        self.assertEqual(len(response.data), 1, "Expected response data to have 1 post")


class TestWork(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.WorkViewSet.as_view({"get": "list"})
        self.uri = "/works/"
        Work.objects.create(
            slug="published",
            title="Published",
            type="art",
            published_at=timezone.now() - timedelta(hours=2),
        )
        Work.objects.create(
            slug="published-future",
            title="Published Future",
            type="code",
            published_at=timezone.now() + timedelta(hours=2),
        )

    def test_list_filter(self):
        request = self.factory.get(self.uri)
        response = self.view(request)

        self.assertEqual(Work.objects.count(), 2, "Expected to find 2 saved works")

        self.assertEqual(len(response.data), 1, "Expected response data to have 1 work")
