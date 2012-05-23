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
        entry = Entry.objects.create(method='GET',
                path='/', meta='HTTP_HOST: localhost')
        entry.save()
        response = self.client.get(reverse('logs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('logs' in response.context)
        self.assertContains(response, 'GET')

        response = self.client.get(reverse('logs_detail', args=[entry.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('entry' in response.context)
        self.assertContains(response, 'HTTP_HOST')
