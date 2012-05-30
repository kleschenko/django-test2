import os
import sys
from cStringIO import StringIO
from django.db import models
from django.test import TestCase
from django.template import Template, Context
from django.core.urlresolvers import reverse
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from contacts.models import Person, ActionsEntry, log_operations


class HttpTest(TestCase):
    def test_contacts_home(self):
        response = self.client.get(reverse('contacts_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(person.name)
        self.assertContains(response, 'Contacts')

    def test_context_processor(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('settings' in response.context)

    def test_contacts_edit_get(self):
        response = self.client.get(reverse('contacts_edit'))
        self.assertEqual(response.status_code, 302)
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('contacts_edit'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

    def test_contacts_edit_post(self):
        self.client.login(username='admin', password='admin')
        form_data = {'name': 'Test', 'surname': 'Surname',
                'birth_date': '1970-01-01',
                'bio': 'Bio', 'email': 'test@example.com'}
        response = self.client.post(reverse('contacts_edit'), form_data)
        self.assertEqual(response.status_code, 302)
        person = Person.objects.get(pk=1)
        self.assertEqual(person.name, 'Test')

    def test_contacts_upload(self):
        self.client.login(username='admin', password='admin')
        image_path = 'fixtures/test_upload.jpg'
        fname = os.path.splitext(os.path.basename(image_path))[0]
        test_upload_path = os.path.join(os.path.split(__file__)[0], image_path)
        f = open(test_upload_path, 'rb')
        post_data = {'name': 'Test', 'surname': 'Surname',
                'birth_date': '1970-01-01', 'bio': 'Bio',
                'email': 'test@example.com', 'photo': f}
        self.client.post(reverse('contacts_edit'), post_data)
        f.close()
        person = Person.objects.get(pk=1)
        self.assertTrue(fname in person.photo.name)
        os.remove(person.photo.path)

    def test_contacts_ajax(self):
        self.client.login(username='admin', password='admin')
        form_data = {'name': 'Test', 'surname': 'Surname',
                'birth_date': '1970-01-01',
                'bio': 'Bio', 'email': 'test@example.com'}
        response = self.client.post(reverse('contacts_edit'), form_data,
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        person = Person.objects.get(pk=1)
        self.assertEqual(person.name, 'Test')
        form_data = {'name': 'Test', 'surname': 'Surname'}
        response = self.client.post(reverse('contacts_edit'), form_data,
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)

    def test_template_tag(self):
        user = User.objects.all()[0]
        out = Template(
                "{% load object_url %}"
                "{% edit_link some_obj %}"
            ).render(Context({'some_obj': user}))
        self.assertTrue('auth/user' in out)


class CommandTest(TestCase):
    def test_command(self):
        app = models.get_app('contacts')
        app_models = models.get_models(app)
        self.assertTrue(app_models)
        ct = ContentType.objects.get_for_model(app_models[0])
        model_name = ct.model
        saved_streams = sys.stdout, sys.stderr
        out = StringIO()
        err = StringIO()
        sys.stdout = out
        sys.stderr = err
        call_command('list_models')
        response = out.getvalue()
        out.close()
        self.assertTrue(model_name in response)
        response = err.getvalue()
        err.close()
        self.assertTrue(model_name in response)
        sys.stdout, sys.stderr = saved_streams

    def test_signal(self):
        post_save.connect(log_operations)
        actions_count = ActionsEntry.objects.count()
        person = Person.objects.get(pk=1)
        person.name = 'Test'
        person.save()
        entries = ActionsEntry.objects.order_by('-dtime')
        new_actions_count = entries.count()
        self.assertEqual(new_actions_count, actions_count + 1)
        self.assertEqual(entries[0].action, 'changed')
