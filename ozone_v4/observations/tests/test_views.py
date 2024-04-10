from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest

from observations.forms import ObservationsForm
from observations.models import Observations


class TestOservationsViews(TestCase):

    def setUp(self):
        self.url = reverse('observ-info-url')

    def test_observations_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'observations.html')

    def test_observations_page_GET_body(self):
        form_values = {
            'start_date': '2024-01-01',
            'end_date': '2025-01-01',
            'parameter': '',
            'city': ''
        }

        response = self.client.get(self.url, data=form_values)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/csv')
        self.assertEqual(response.headers['Content-Disposition'], f'attachment; filename="observations.csv"')
