#!/bin/bash

celery -A config.settings beat -l INFO
