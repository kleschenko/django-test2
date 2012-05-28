#!/usr/bin/env bash

python2 manage.py list_models 2> `date +'%Y.%m.%d'`.dat
