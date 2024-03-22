from django.test import TestCase
from datetime import datetime

from main_app.models import (
    News, Article, Document, Devices, DevicesCharacteristic
)


class MainAppModelsTest(TestCase):

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

    def test_news_model(self):
        self.assertEqual(
            self.news_test.__str__(),
            f'News | {self.news_test.title} | {self.date_test}'
        )
        self.assertEqual(self.news_test.status, 'PB')

    def test_article_model(self):
        self.assertEqual(
            self.article_test.__str__(),
            f'Article | {self.article_test.title} | {self.date_test}'
        )
        self.assertEqual(self.article_test.status, 'PB')

    def test_document_model(self):
        self.assertEqual(self.document_test.__str__(), self.document_test.name)

    def test_devices_model(self):
        self.assertEqual(self.devices_test.__str__(), self.devices_test.name)
        self.assertTrue(self.devices_test.characteristics.all())

    def test_devices_characteristics_model(self):
        char_example = self.devices_characteristics_test

        self.assertEqual(
            char_example.__str__(),
            f'{char_example.device}|{char_example.characteristic_name}'
        )




