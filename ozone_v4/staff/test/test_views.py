from django.test import TestCase
from django.urls import reverse

from staff.models import Worker


class TestWorkerView(TestCase):

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

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/staff/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("workers-list-url"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("workers-list-url"))
        self.assertTemplateUsed(response, "team.html")


class TestWorkerSingleView(TestCase):
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

    def test_url_exists_at_correct_location(self):
        response = self.client.get(f"/staff/{self.worker_test.id}/")
        self.assertEqual(response.status_code, 200)

    def test_url_redirection(self):
        response = self.client.get("/staff/11111111/")
        self.assertEqual(response.status_code, 302)

    def test_template_name_correct(self):
        response = self.client.get(f"/staff/{self.worker_test.id}/")
        self.assertTemplateUsed(response, "team-single.html")
