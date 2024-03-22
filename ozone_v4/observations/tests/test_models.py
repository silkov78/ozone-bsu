from django.test import TestCase
from datetime import datetime

from observations.models import Observations, AnnualReport


class ObservationsTest(TestCase):

    def test_observations_creation(self):
        date_example = datetime.strptime('29-02-2024', '%d-%m-%Y').date()

        new_observ = Observations.objects.create(
            date=date_example,
            common_ozone_minsk=22.0,
            ground_ozone_minsk=31.1,
        )

        self.assertEqual(new_observ.__str__(), f'{new_observ.date}')
        self.assertEqual(new_observ.weekday, 'Thursday')

    def test_annual_report_creation(self):
        new_report = AnnualReport.objects.create(
            year=2009,
            report_file='mock file'
        )

        self.assertEqual(new_report.__str__(), f'Отчёт за 2009 год')

