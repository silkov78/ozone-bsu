from django.test import TestCase
from django.urls import reverse
import tempfile
import datetime

from main_app.models import News


class TestViews(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_observations(self):
        response = self.client.get('/observations/')
        self.assertEqual(response.status_code, 200)

    def test_news(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_news_item(self):
        news_item = News.objects.create(
            id=1,
            title='First News',
            subtitle='Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            image_logo=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            body='Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            published=datetime.date.today()

        )
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

    def test_news_item_redirect(self):
        response = self.client.get('/blog/1111111111111/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/blog/')
