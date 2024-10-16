#!/bin/bash

celery -A config.settings worker -l info -c 4 -Q general
