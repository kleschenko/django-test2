from django.test import TestCase
from django.core.urlresolvers import reverse


class HttpTest(TestCase):
    def test_contacts_home(self):
        response = self.client.get(reverse('contacts_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(person.name)
        self.assertContains(response, 'Contacts')
