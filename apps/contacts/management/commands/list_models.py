from django.core.management.base import NoArgsCommand
from django.db import models


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        app_models = models.get_models()
        for model in app_models:
            output = 'Model: %20s,\tObjects: %s\n' % (model.__name__,
                model.objects.count())
            self.stdout.write(output)
            self.stderr.write('error: ' + output)
