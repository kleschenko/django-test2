from django.test import TestCase
from django.core.urlresolvers import reverse
from logs.models import Entry


class HttpTest(TestCase):
    def setUp(self):
        self.client.get('/')
        self.entry = Entry.objects.all()[0]

    def test_logs_list(self):
        entries_count = Entry.objects.count()
        response = self.client.get('/my_not_existing_url')
        new_entries_count = Entry.objects.count()
        response = self.client.get(reverse('logs_list'))
        self.assertEqual(new_entries_count - entries_count, 1)
        self.assertTrue('logs' in response.context)
        self.assertContains(response, 'GET')
        self.assertContains(response, 'my_not_existing_url')

    def test_ajax_logs_list(self):
        response = self.client.get(reverse('logs_list'),
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_detail_get(self):
        response = self.client.get(reverse('logs_detail', args=[self.entry.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('entry' in response.context)

    def test_detail_post(self):
        priority = self.entry.priority
        form_data = {'rate': '1'}
        response = self.client.post(reverse('logs_detail',
            args=[self.entry.id]), form_data)
        self.assertEqual(response.status_code, 200)
        upd_entry = Entry.objects.get(id=self.entry.id)
        self.assertEqual(priority + 1, upd_entry.priority)
        form_data = {'rate': '-1'}
        self.client.post(reverse('logs_detail',
            args=[self.entry.id]), form_data)
        upd_entry = Entry.objects.get(id=self.entry.id)
        self.assertEqual(priority, upd_entry.priority)

    def test_ajax_detail_post(self):
        priority = self.entry.priority
        form_data = {'rate': '1'}
        response = self.client.post(reverse('logs_detail',
            args=[self.entry.id]), form_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        upd_entry = Entry.objects.get(id=self.entry.id)
        self.assertEqual(priority + 1, upd_entry.priority)
        form_data = {'rate': 'bad_value'}
        response = self.client.post(reverse('logs_detail',
            args=[self.entry.id]), form_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
