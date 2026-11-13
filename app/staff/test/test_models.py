from django.test import TestCase
from datetime import datetime

from staff.models import (
    Worker, Education, Career,
    Reward, ScienceInterest, Publication
)


class TestStaffModels(TestCase):

    def setUp(self):
        # Worker
        self.worker_test = Worker.objects.create(
            last_name='Ivanov',
            first_name='Ivan',
            middle_name='Ivanovich',
            photo='some_photo.jpg',
            ordering=1,
            academic_rank='ScienceGod',
            position='LabaratoryGod',
            google_academy='ivanov@gmail.com'
        )

        # Education
        self.education_test = Education.objects.create(
            worker=self.worker_test,
            study_finishing=1990,
            study_description='Lorem ipsum lorem ipsum',
        )

        # Career
        self.career_test = Career.objects.create(
            worker=self.worker_test,
            career_start=1990,
            career_period='Lorem ipsum lorem ipsum',
            career_description='Lorem ipsum lorem ipsum',
        )

        # Reward
        self.reward_test = Reward.objects.create(
            worker=self.worker_test,
            reward_year=1990,
            reward_description='Lorem ipsum lorem ipsum',
        )

        # Devices Characteristics
        self.science_interest_test = ScienceInterest.objects.create(
            worker=self.worker_test,
            science_interest='Lorem ipsum lorem ipsum',
        )

        self.publication_test = Publication.objects.create(
            worker=self.worker_test,
            publication_year=1990,
            publication_description='Lorem ipsum lorem ipsum',
            publication_link='Lorem ipsum lorem ipsum',
        )

    def test_woker_str(self):
        self.assertEqual(
            self.worker_test.__str__(),
            f'{self.worker_test.last_name} {self.worker_test.first_name}'
        )

    def test_worker_foreign_keys(self):
        self.assertTrue(self.worker_test.education.all())
        self.assertTrue(self.worker_test.career.all())
        self.assertTrue(self.worker_test.rewards.all())
        self.assertTrue(self.worker_test.science_interests.all())
        self.assertTrue(self.worker_test.publications.all())

    def test_education_str(self):
        self.assertEqual(
            self.education_test.__str__(),
            f'{self.education_test.worker} {self.education_test.study_finishing}'
        )

    def test_career_str(self):
        self.assertEqual(
            self.career_test.__str__(),
            f'{self.career_test.worker} {self.career_test.career_start}'
        )

    def test_reward_str(self):
        self.assertEqual(
            self.reward_test.__str__(),
            f'{self.reward_test.worker} {self.reward_test.reward_year}'
        )

    def test_science_interest_str(self):
        self.assertEqual(
            self.science_interest_test.__str__(),
            f'{self.science_interest_test.worker} {self.science_interest_test.science_interest}'
        )

    def test_publication_str(self):
        self.assertEqual(
            self.publication_test.__str__(),
            f'{self.publication_test.worker} {self.publication_test.publication_year}'
        )
