MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_test.settings $(MANAGE) test contacts logs

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_test.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_test.settings $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_test.settings $(MANAGE) migrate --noinput
