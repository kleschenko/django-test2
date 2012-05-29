#!/usr/bin/env bash

python manage.py list_models 2> `date +'%Y.%m.%d'`.dat
