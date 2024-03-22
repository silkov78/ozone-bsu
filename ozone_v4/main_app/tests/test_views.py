from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from main_app.models import (
    News, Article, Document, Devices, DevicesCharacteristic
)

class TestHomepageView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()

        # News
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

        # Article
        self.article_test = Article.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum' * 10,
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

        # Document
        self.document_test = Document.objects.create(
            name='The example news',
            description='Lorem ipsum lorem ipsum',
            document='some_document'
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("main-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("main-page-url"))
        self.assertTemplateUsed(response, "index.html")

    def test_template_content(self):
        response = self.client.get(reverse("main-page-url"))
        self.assertContains(response,  self.news_test.title)
        self.assertContains(response,  self.article_test.title)


# Blog
class TestBlogView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertTemplateUsed(response, "blog.html")

    def test_template_content(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertContains(response,  self.news_test.title)


class TestBlogSingleView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/blog/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertTemplateUsed(response, "blog-single.html")

    def test_template_content(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertContains(response,  self.news_test.title)


# Documents
class TestDocumentView(TestCase):

    def setUp(self):
        # Document
        self.document_test = Document.objects.create(
            name='The example news',
            description='Lorem ipsum lorem ipsum',
            document='some_document'
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/documents/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("documents-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("documents-page-url"))
        self.assertTemplateUsed(response, "documents.html")

    def test_template_content(self):
        response = self.client.get(reverse("documents-page-url"))
        self.assertContains(response,  self.document_test.name)


# Article
class TestArticleView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.article_test = Article.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/articles/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("articles-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("articles-page-url"))
        self.assertTemplateUsed(response, "articles.html")

    def test_template_content(self):
        response = self.client.get(reverse("articles-page-url"))
        self.assertContains(response,  self.article_test.title)


class TestArticleSingleView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.article_test = Article.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/articles/{self.article_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/articles/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/articles/{self.article_test.id}/")
        self.assertTemplateUsed(response, "article-single.html")

    def test_template_content(self):
        response = self.client.get(f"/articles/{self.article_test.id}/")
        self.assertContains(response,  self.article_test.title)


# Search
class TestBlogView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertTemplateUsed(response, "blog.html")

    def test_template_content(self):
        response = self.client.get(reverse("blog-page-url"))
        self.assertContains(response,  self.news_test.title)


class TestBlogSingleView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/blog/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertTemplateUsed(response, "blog-single.html")

    def test_template_content(self):
        response = self.client.get(f"/blog/{self.news_test.id}/")
        self.assertContains(response,  self.news_test.title)


# Search
class TestSearchView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )
        self.search_data={'search': 'example'}

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/search/", data=self.search_data)
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("search-page-url"), data=self.search_data)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("search-page-url"), data=self.search_data)
        self.assertTemplateUsed(response, "search.html")

    def test_template_content_without_GET_data(self):
        response = self.client.get(
            reverse("search-page-url"),
            data={'search': ''}
        )
        self.assertContains(response,  self.news_test.title)

    def test_template_content_GET_data(self):
        response = self.client.get(reverse("search-page-url"), data=self.search_data)
        self.assertContains(response,  self.news_test.title)


class TestSearchSingleView(TestCase):

    def setUp(self):
        self.date_test = datetime.strptime('29-02-2024', '%d-%m-%Y').date()
        self.news_test = News.objects.create(
            title='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            image_logo='some_image',
            body='Lorem ipsum lorem ipsum',
            published=self.date_test
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/search/{self.news_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/search/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/search/{self.news_test.id}/")
        self.assertTemplateUsed(response, "blog-single.html")

    def test_template_content(self):
        response = self.client.get(f"/search/{self.news_test.id}/")
        self.assertContains(response,  self.news_test.title)


# Devices
class TestDevicesView(TestCase):

    def setUp(self):
        # Devices
        self.devices_test = Devices.objects.create(
            name='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            description='Lorem ipsum lorem ipsum',
            main_image='some_document'
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/devices/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("devices-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("devices-page-url"))
        self.assertTemplateUsed(response, "devices.html")

    def test_template_content_GET_data(self):
        response = self.client.get(reverse("devices-page-url"))
        self.assertContains(response,  self.devices_test.name)


class TestSearchSingleView(TestCase):

    def setUp(self):
        # Devices
        self.devices_test = Devices.objects.create(
            name='The example news',
            subtitle='Lorem ipsum lorem ipsum',
            description='Lorem ipsum lorem ipsum',
            main_image='some_document'
        )

        # Devices Characteristics
        self.devices_characteristics_test = DevicesCharacteristic.objects.create(
            device=self.devices_test,
            characteristic_name='Lorem ipsum lorem ipsum',
            characteristic_value='Lorem',
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/devices/{self.devices_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/devices/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/devices/{self.devices_test.id}/")
        self.assertTemplateUsed(response, "devices-single.html")

    def test_template_content(self):
        response = self.client.get(f"/devices/{self.devices_test.id}/")
        self.assertContains(response,  self.devices_test.name)
        self.assertContains(response,  self.devices_characteristics_test.characteristic_name)


# About
class TestAboutView(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about-page-url"))
        self.assertTemplateUsed(response, "about.html")


# Cookies
class TestCookiesView(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/cookies/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("cookies-page-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("cookies-page-url"))
        self.assertTemplateUsed(response, "cookies.html")
