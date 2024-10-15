#!/bin/bash

celery -A config.settings worker -Q general
