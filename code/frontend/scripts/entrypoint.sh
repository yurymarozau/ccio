#!/bin/bash

ENV_FILE=".env"

printenv > "$ENV_FILE" && $1
