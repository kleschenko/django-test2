import sys
from django.db import models
from django.db.models.signals import post_save, post_delete


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birth_date = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField(blank=True)
    skype = models.CharField(max_length=32, blank=True)
    other_contacts = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.surname, self.name)


class ActionsEntry(models.Model):
    dtime = models.DateTimeField(auto_now_add=True)
    model_name = models.CharField(max_length=30)
    action = models.CharField(max_length=10)

    def __unicode__(self):
        return '[%s]: %s %s' % (self.dtime.strftime('%d.%m.%Y %H:%M'),
                self.action, self.model_name)

    class Meta:
        verbose_name_plural = 'actions'


def log_operations(sender, signal, **kwargs):
    if sender != ActionsEntry:
        if signal == post_save:
            action = 'created' if 'created' in kwargs and kwargs['created'] else 'changed'
        else:
            action = 'deleted'
        action_entry = ActionsEntry(model_name=sender.__name__, action=action)
        action_entry.save()

if not 'syncdb' in sys.argv and not 'migrate' in sys.argv and not 'test' in sys.argv:
    post_save.connect(log_operations)
    post_delete.connect(log_operations)
