from django.core.management.base import NoArgsCommand
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        app_models = models.get_models()
        for model in app_models:
            ct = ContentType.objects.get_for_model(model)
            output = 'Model: %20s,\tObjects: %s\n' % (ct.app_label + '.' + ct.model,
                model.objects.count())
            self.stdout.write(output)
            self.stderr.write('error: ' + output)
