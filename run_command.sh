#!/usr/bin/env bash

VENV=../
source $VENV/bin/activate && PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=django_test.settings python manage.py list_models 2> `date +'%Y.%m.%d'`.dat
