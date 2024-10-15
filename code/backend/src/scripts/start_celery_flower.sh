#!/bin/bash

celery -A config.settings.celery flower
