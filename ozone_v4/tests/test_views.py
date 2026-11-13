"""Smoke-тесты страниц нового фронта и редиректов со старых адресов."""
from datetime import date

from django.test import TestCase
from django.urls import reverse

from main_app.models import News, Devices, Article
from observations.models import Observations
from staff.models import Worker


class SiteViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title='Новость', image_logo='main/news/x.jpg', published=date(2026, 11, 1),
            body='Текст. Ссылка: https://wmo.int/a', source_url='https://wmo.int/a')
        cls.draft = News.objects.create(
            title='Черновик', image_logo='main/news/y.jpg', published=date(2026, 11, 2), body='—', status='DF')
        cls.worker = Worker.objects.create(last_name='Иванов', first_name='Иван', middle_name='Иванович', ordering=1)
        cls.device = Devices.objects.create(name='ПИОН', subtitle='прибор', description='описание', main_image='main/devices/d.jpg')
        cls.article = Article.objects.create(title='Статья', image_logo='main/news/z.jpg', published=date(2026, 1, 1), body='текст')
        for d in range(1, 11):
            Observations.objects.create(date=date(2026, 11, d), total_ozone_minsk=300 + d, total_uvi_minsk=1.0)

    def test_pages_ok(self):
        for name, args in [
            ('main-page-url', []), ('news-list-url', []), ('news-item-url', [self.news.pk]),
            ('about-page-url', []), ('science-page-url', []), ('observations-url', []),
            ('search-page-url', []), ('cookies-page-url', []), ('workers-detail-url', [self.worker.pk]),
            ('devices-item-url', [self.device.pk]), ('articles-item-url', [self.article.pk]),
        ]:
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name, args=args)).status_code, 200)

    def test_draft_news_hidden(self):
        self.assertEqual(self.client.get(reverse('news-item-url', args=[self.draft.pk])).status_code, 404)
        self.assertNotContains(self.client.get(reverse('news-list-url')), 'Черновик')

    def test_news_source_shown(self):
        self.assertContains(self.client.get(reverse('news-item-url', args=[self.news.pk])), 'wmo.int')

    def test_search(self):
        self.assertContains(self.client.get(reverse('search-page-url'), {'q': 'Новость'}), 'Новость')

    def test_old_urls_redirect(self):
        for old, new in [
            ('/blog/', '/news/'), (f'/blog/{self.news.pk}/', f'/news/{self.news.pk}/'),
            ('/observations/info/', '/observations/'), ('/observations/download/', '/observations/'),
            ('/staff/', '/about/#team'), ('/articles/', '/science/#research'), ('/devices/', '/science/#devices'), ('/documents/', '/about/#documents'),
        ]:
            with self.subTest(old=old):
                self.assertRedirects(self.client.get(old), new, status_code=301, fetch_redirect_response=False)

    def test_export_csv(self):
        r = self.client.get(reverse('observations-export-url'), {'from': '2026-11-02', 'to': '2026-11-03'})
        self.assertEqual(r['Content-Type'], 'text/csv; charset=utf-8')
        lines = r.content.decode().strip().splitlines()
        self.assertEqual(len(lines), 3)  # заголовок + 2 дня
        self.assertTrue(lines[0].startswith('date,total_ozone_minsk'))

    def test_export_xlsx(self):
        r = self.client.get(reverse('observations-export-url'), {'format': 'xlsx'})
        self.assertIn('spreadsheetml', r['Content-Type'])

    def test_chart_api(self):
        data = self.client.get(reverse('observ-chart-data'), {'range': 'week'}).json()
        self.assertEqual(data['labels'][-1], '2026-11-10')
