"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from logs.models import Entry


class HttpTest(TestCase):
    def test_logs(self):
        entries_count = Entry.objects.count()
        response = self.client.get('/my_not_existing_url')
        new_entries_count = Entry.objects.count()
        response = self.client.get(reverse('logs_list'))
        self.assertEqual(new_entries_count - entries_count, 1)
        self.assertTrue('logs' in response.context)
        self.assertContains(response, 'GET')
        self.assertContains(response, 'my_not_existing_url')
