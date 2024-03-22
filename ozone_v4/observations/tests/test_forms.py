from django.test import TestCase

from observations.forms import ObservationsForm
from observations.models import Observations


class TestForms(TestCase):
    def test_observations_form_valid_data(self):
        form = ObservationsForm(
            data={
                'start_date': '2024-01-01',
                'end_date': '2025-01-01',
                'parameter': '',
                'city': 'naroch'
            })

        self.assertTrue(form.is_valid())

    def test_observations_form_no_data(self):
        form = ObservationsForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

