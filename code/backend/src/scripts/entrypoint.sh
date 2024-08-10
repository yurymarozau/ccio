#!/bin/bash

./scripts/wait-for-it.sh ${DATABASE_HOST}:${DATABASE_PORT} --timeout=${WFI_TIMEOUT} -- $1
