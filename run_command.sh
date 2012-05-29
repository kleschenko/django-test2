#!/usr/bin/env bash

PROJECT_ROOT=`pwd`
VENV_ROOT=`dirname $PROJECT_ROOT`

source $VENV_ROOT/bin/activate && python $PROJECT_ROOT/manage.py list_models 2> `date +'%Y.%m.%d'`.dat
